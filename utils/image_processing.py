# -*- coding: utf-8 -*-
from PIL import Image

def load_image(image_path: str) -> Image.Image:
    image = Image.open(image_path).convert("RGB")
    """
    Mục đích:
        Tải một ảnh từ đường dẫn và chuyển thành đối tượng PIL Image.

    Tham số:
        image_path (str): Đường dẫn đến file ảnh.

    Trả về:
        Image.Image: Đối tượng ảnh của thư viện Pillow.
    """
    # Logic chính:
    # 1. Dùng `Image.open(image_path)`.
    # 2. Chuyển ảnh sang định dạng RGB: `img.convert("RGB")`.
    # 3. Xử lý exception nếu file không tồn tại hoặc không phải file ảnh.
    pass