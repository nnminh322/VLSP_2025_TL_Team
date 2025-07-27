# -*- coding: utf-8 -*-
from typing import List, Tuple
from PIL import Image

class Reranker:
    """
    Mục đích:
        Sử dụng một model Cross-Encoder để đánh giá lại và xếp hạng mức độ
        liên quan giữa một query và các văn bản ứng viên.
    """

    def __init__(self, model_name: str, device: str = "cpu"):
        """
        Mục đích:
            Khởi tạo model Cross-Encoder từ Hugging Face.

        Tham số:
            model_name (str): Tên của model trên Hugging Face Hub.
            device (str): Thiết bị để chạy model ('cpu' hoặc 'cuda').
        """
        # Logic chính:
        # 1. Tải model và tokenizer từ `model_name` bằng `transformers`.
        #    (Ví dụ: `AutoTokenizer`, `AutoModelForSequenceClassification`)
        # 2. Chuyển model sang thiết bị.
        self.model = None
        self.tokenizer = None
        self.device = device


    def compute_scores(self, query_text: str, documents: List[str]) -> List[float]:
        """
        Mục đích:
            Tính điểm liên quan cho từng cặp (query, document).
            Lưu ý: Cross-encoder hiện tại chủ yếu xử lý text-text.
            Việc tích hợp ảnh vào reranker phức tạp hơn.
            Ở đây, ta giả định reranker chỉ dùng text.

        Tham số:
            query_text (str): Câu query của người dùng.
            documents (List[str]): Danh sách các nội dung văn bản ứng viên.

        Trả về:
            List[float]: Một danh sách các điểm số tương ứng với mỗi document.

        Logic chính:
            1. Tạo các cặp `(query_text, doc_text)` cho tất cả document.
            2. Sử dụng `self.tokenizer` để chuẩn bị các cặp này cho model.
            3. Đưa dữ liệu đã tokenize qua `self.model`.
            4. Lấy ra điểm số (logits) và áp dụng hàm sigmoid/softmax để
               chuyển thành xác suất/điểm số từ 0 đến 1.
            5. Trả về danh sách các điểm số.
        """
        pass