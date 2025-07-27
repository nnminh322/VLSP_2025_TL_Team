# -*- coding: utf-8 -*-
from typing import List, Dict, Any, Tuple
import numpy as np
from qdrant_client import QdrantClient, models

class QdrantVectorStore:
    """
    Mục đích:
        Một lớp bao bọc cho client của Qdrant để thực hiện việc
        lưu trữ và tìm kiếm vector.
    """
    def __init__(self, host: str, port: int, collection_name: str, dimension: int):
        """
        Tham số:
            host (str): Địa chỉ host của Qdrant.
            port (int): Cổng của Qdrant.
            collection_name (str): Tên collection để lưu trữ vector.
            dimension (int): Số chiều của vector.
        """
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = collection_name
        self.dimension = dimension
        # Tự động tạo collection nếu chưa có
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(size=self.dimension, distance=models.Distance.COSINE),
        )

    def add(self, vectors: np.ndarray, payloads: List[Dict[str, Any]]):
        """
        Mục đích:
            Thêm các vector và metadata (payload) vào collection.

        Tham số:
            vectors (np.ndarray): Mảng NumPy 2D chứa các vector.
            payloads (List[Dict[str, Any]]): Danh sách các metadata tương ứng
                                              với từng vector.
        """
        self.client.upsert(
            collection_name=self.collection_name,
            points=models.Batch(
                ids=list(range(len(vectors))), # Có thể dùng ID tường minh hơn
                vectors=vectors.tolist(),
                payloads=payloads
            ),
            wait=True
        )

    def search(self, query_vector: np.ndarray, k: int) -> List[Dict[str, Any]]:
        """
        Mục đích:
            Tìm kiếm k vector gần nhất và trả về kết quả cùng với payload.

        Tham số:
            query_vector (np.ndarray): Vector query có shape (1, dimension).
            k (int): Số lượng kết quả cần tìm.

        Trả về:
            List[Dict[str, Any]]: Danh sách các kết quả, mỗi kết quả là một dict
                                  chứa 'id', 'score', và 'payload'.
        """
        hits = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector.flatten().tolist(),
            limit=k
        )
        return [hit.model_dump() for hit in hits] # .dict() cho phiên bản cũ