# -*- coding: utf-8 -*-
from typing import List, Dict, Any

def preprocess_documents(documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Mục đích:
        Làm sạch và tiền xử lý các văn bản luật để chuẩn bị cho việc
        tạo embedding.

    Tham số:
        documents (List[Dict[str, Any]]): Danh sách các văn bản thô
                                            từ hàm `load_documents`.

    Trả về:
        List[Dict[str, Any]]: Danh sách các văn bản đã được xử lý.
                               Có thể thêm các trường mới nếu cần.

    Logic chính:
        1. Lặp qua từng document trong danh sách `documents`.
        2. Với mỗi document, lấy ra trường 'text'.
        3. Thực hiện các bước làm sạch:
           - Xóa các ký tự thừa, HTML tags (nếu có).
           - Chuẩn hóa khoảng trắng.
           - Có thể cân nhắc việc chia văn bản dài thành các đoạn nhỏ (chunking)
             nếu một điều luật quá dài. Tuy nhiên, với luật, thường giữ
             nguyên mỗi điều là một đơn vị.
        4. Cập nhật lại trường 'text' đã làm sạch cho document.
        5. Trả về danh sách documents đã xử lý.
    """
    # Logic chính:
    # 1. Lặp qua từng document.
    # 2. Lấy ra `doc['text']` và áp dụng các hàm xử lý từ `utils.text_processing`.
    # 3. Trả về danh sách đã cập nhật.
    pass