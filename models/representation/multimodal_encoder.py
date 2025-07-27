# -*- coding: utf-8 -*-
from typing import List
import numpy as np
from PIL import Image

class MultimodalEncoder:
    """
    Mục đích:
        Class này chịu trách nhiệm biến đầu vào đa phương tiện (ảnh và text)
        thành một vector embedding duy nhất.
    """

    def __init__(self, model_name: str, device: str = "cpu"):
        """
        Mục đích:
            Khởi tạo model encoder từ Hugging Face.

        Tham số:
            model_name (str): Tên của model trên Hugging Face Hub (ví dụ: 'vinai/vinai-clip-vit-b-16').
            device (str): Thiết bị để chạy model ('cpu' hoặc 'cuda').
        """
        # Logic chính:
        # 1. Tải model và processor từ `model_name` bằng thư viện `transformers`.
        #    (Ví dụ: `AutoProcessor.from_pretrained`, `AutoModel.from_pretrained`)
        # 2. Chuyển model sang thiết bị (`.to(device)`).
        self.model = None
        self.processor = None
        self.device = device

    def encode(self, texts: List[str], images: List[Image.Image]) -> np.ndarray:
        """
        Mục đích:
            Tạo ra các vector embedding từ một batch các cặp text và ảnh.

        Tham số:
            texts (List[str]): Một danh sách các câu mô tả.
            images (List[Image.Image]): Một danh sách các đối tượng ảnh PIL.
                                         Danh sách này phải có cùng độ dài với `texts`.

        Trả về:
            np.ndarray: Một mảng NumPy chứa các vector embedding, có shape
                        (batch_size, embedding_dim).

        Logic chính:
            1. Sử dụng `self.processor` để xử lý cả text và ảnh, chuyển chúng
               thành định dạng tensor mà model yêu cầu.
            2. Đưa tensor đã xử lý vào `self.model` để lấy ra embedding.
               Đối với CLIP, có thể lấy `text_features` hoặc `image_features`
               hoặc kết hợp chúng. Với bài toán này, ta sẽ encode riêng rẽ:
               - Khi encode query: lấy `image_features` và `text_features`, rồi kết hợp.
               - Khi encode documents (chỉ có text): chỉ lấy `text_features`.
            3. Chuẩn hóa vector (L2 normalization).
            4. Chuyển tensor kết quả về dạng NumPy array trên CPU.
        """
        pass