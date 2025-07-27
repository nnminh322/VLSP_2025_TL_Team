# -*- coding: utf-8 -*-
from typing import List, Dict, Any
from retrieval.multimodal_retriever import MultimodalRetriever

def calculate_hit_rate_at_k(predictions: List[str], ground_truth_ids: List[str], k: int) -> float:
    """Tính Hit Rate@k."""
    predicted_set = set(predictions[:k])
    ground_truth_set = set(ground_truth_ids)
    return 1.0 if predicted_set.intersection(ground_truth_set) else 0.0

def calculate_mrr_at_k(predictions: List[str], ground_truth_ids: List[str], k: int) -> float:
    """Tính Mean Reciprocal Rank@k."""
    for i, pred_id in enumerate(predictions[:k]):
        if pred_id in ground_truth_ids:
            return 1.0 / (i + 1)
    return 0.0

def evaluate_retriever(retriever: MultimodalRetriever, eval_dataset: List[Dict[str, Any]], k: int) -> Dict[str, float]:
    """
    Mục đích:
        Đánh giá hiệu năng của hệ thống retriever trên một tập dữ liệu kiểm thử.

    Tham số:
        retriever (MultimodalRetriever): Đối tượng retriever cần đánh giá.
        eval_dataset (List[Dict[str, Any]]): Tập dữ liệu đánh giá. Mỗi phần tử
                                             là một dict chứa 'query_text',
                                             'query_image_path', và 'ground_truth_ids'.
        k (int): Ngưỡng để tính các chỉ số (ví dụ: Hit Rate@5).

    Trả về:
        Dict[str, float]: Một dictionary chứa các chỉ số đánh giá trung bình
                          (ví dụ: {'hit_rate_at_k': 0.85, 'mrr_at_k': 0.75}).

    Logic chính:
        1. Khởi tạo các biến để lưu tổng điểm của các chỉ số.
        2. Lặp qua từng mẫu trong `eval_dataset`.
        3. Với mỗi mẫu, lấy query và gọi `retriever.retrieve` để có danh sách dự đoán.
        4. Lấy ra các ID của document được dự đoán.
        5. So sánh danh sách ID dự đoán với `ground_truth_ids`.
        6. Tính các chỉ số như Hit Rate@k, MRR@k cho mẫu hiện tại.
        7. Cộng dồn điểm số.
        8. Sau khi lặp xong, chia tổng điểm cho số lượng mẫu để có giá trị trung bình.
        9. Trả về dict chứa các chỉ số trung bình.
    """
    total_hit_rate = 0
    total_mrr = 0
    num_samples = len(eval_dataset)

    for sample in eval_dataset:
        query_text = sample['query_text']
        # Cần logic để tải ảnh từ sample['query_image_path']
        # query_image = ... 
        
        # Giả sử retriever trả về list các dict có key 'id'
        # retrieved_docs = retriever.retrieve(query_text, query_image, ...)
        # predicted_ids = [doc['id'] for doc in retrieved_docs]
        
        predicted_ids = [] # Placeholder
        ground_truth_ids = sample['ground_truth_ids']

        total_hit_rate += calculate_hit_rate_at_k(predicted_ids, ground_truth_ids, k)
        total_mrr += calculate_mrr_at_k(predicted_ids, ground_truth_ids, k)
        
    return {
        f"hit_rate_at_{k}": total_hit_rate / num_samples if num_samples > 0 else 0,
        f"mrr_at_{k}": total_mrr / num_samples if num_samples > 0 else 0,
    }