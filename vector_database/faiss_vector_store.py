# -*- coding: utf-8 -*-
from typing import List, Tuple
import numpy as np

class FaissVectorStore:
    """
    Mục đích:
        Một lớp bao bọc (wrapper) cho thư viện FAISS để thực hiện việc
        lưu trữ, tìm kiếm, và quản lý vector embedding.
    """

    def __init__(self, dimension: int):
        """
        Mục đích:
            Khởi tạo một chỉ mục (index) FAISS trống.

        Tham số:
            dimension (int): Số chiều của vector embedding.
        """
        # Logic chính:
        # 1. Import thư viện `faiss`.
        # 2. Khởi tạo một chỉ mục, ví dụ `faiss.IndexFlatL2(dimension)`.
        self.index = None

    def add(self, vectors: np.ndarray):
        """
        Mục đích:
            Thêm các vector vào chỉ mục FAISS.

        Tham số:
            vectors (np.ndarray): Một mảng NumPy 2D có shape (num_vectors, dimension).
        """
        # Logic chính:
        # 1. Dùng `self.index.add(vectors)`.
        pass

    def search(self, query_vector: np.ndarray, k: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Mục đích:
            Tìm kiếm k vector gần nhất với một vector query.

        Tham số:
            query_vector (np.ndarray): Vector query có shape (1, dimension).
            k (int): Số lượng hàng xóm gần nhất cần tìm.

        Trả về:
            Tuple[np.ndarray, np.ndarray]:
                - distances: Khoảng cách từ query đến các vector kết quả.
                - indices: Chỉ số (ID) của các vector kết quả trong index.
        """
        # Logic chính:
        # 1. Dùng `self.index.search(query_vector, k)`.
        return (None, None)

    def save(self, file_path: str):
        """
        Mục đích:
            Lưu chỉ mục FAISS ra file.

        Tham số:
            file_path (str): Đường dẫn để lưu file chỉ mục.
        """
        # Logic chính:
        # 1. Import `faiss`.
        # 2. Dùng `faiss.write_index(self.index, file_path)`.
        pass

    def load(self, file_path: str):
        """
        Mục đích:
            Tải một chỉ mục FAISS từ file.

        Tham số:
            file_path (str): Đường dẫn đến file chỉ mục đã lưu.
        """
        # Logic chính:
        # 1. Import `faiss`.
        # 2. Dùng `faiss.read_index(file_path)`.
        # 3. Gán chỉ mục đã tải cho `self.index`.
        pass