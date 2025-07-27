# -*- coding: utf-8 -*-
import re

def normalize_whitespace(text: str) -> str:
    """
    Mục đích:
        Chuẩn hóa các khoảng trắng thừa trong văn bản.

    Trả về:
        str: Văn bản đã được chuẩn hóa khoảng trắng.
    """
    return re.sub(r'\s+', ' ', text).strip()

def remove_special_chars(text: str) -> str:
    """
    Mục đích:
        Loại bỏ các ký tự không cần thiết (tùy chỉnh theo yêu cầu).

    Trả về:
        str: Văn bản đã được làm sạch.
    """
    # Ví dụ đơn giản, có thể cần phức tạp hơn
    return re.sub(r'[^a-zA-Z0-9\s\.,áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ]', '', text)