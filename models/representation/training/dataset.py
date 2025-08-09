# -*- coding: utf-8 -*-
from typing import List, Dict, Any
from torch.utils.data import Dataset
from PIL import Image

class EncoderDataset(Dataset):
    """
    Mục đích:
        Tạo một đối tượng Dataset của PyTorch để cung cấp dữ liệu cho việc
        training model encoder. Dataset này hoạt động dựa trên các cặp
        (ảnh, text) và nhãn (nếu có).
    """
    def __init__(self, data: List[Dict[str, Any]], image_dir: str, processor):
        """
        Tham số:
            data (List[Dict[str, Any]]): Danh sách dữ liệu, mỗi phần tử là một dict
                                         chứa 'image_file' và 'caption'.
            image_dir (str): Thư mục chứa các file ảnh.
            processor: Processor của model (ví dụ: BLIPProcessor) để xử lý ảnh và text.
        """
        self.image_dir = image_dir
        self.processor = processor

    def __len__(self) -> int:
        """Trả về số lượng mẫu trong dataset."""
        return len(self.data)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Mục đích:
            Lấy một mẫu dữ liệu tại vị trí `idx`.

        Tham số:
            idx (int): Chỉ số của mẫu cần lấy.

        Trả về:
            Dict[str, Any]: Một dictionary chứa các tensor đã được xử lý,
                            sẵn sàng để đưa vào model. Ví dụ: {'input_ids': ...,
                            'pixel_values': ..., 'attention_mask': ...}.
        Logic chính:
            1. Lấy thông tin mẫu tại `self.data[idx]`.
            2. Tải ảnh từ `self.image_dir` và `item['image_file']`.
            3. Lấy caption từ `item['caption']`.
            4. Sử dụng `self.processor` để xử lý cả ảnh và caption.
            5. Trả về kết quả đã được xử lý.
        """
        item = self.data[idx]
        image_path = f"{self.image_dir}/{item['image_file']}"
        image = Image.open(image_path).convert("RGB")
        text = item['caption']
        
        # Processor sẽ xử lý và trả về dict đúng format model cần
        inputs = self.processor(text=[text], images=image, return_tensors="pt", padding=True)
        # Squeeze để loại bỏ chiều batch không cần thiết
        return {key: val.squeeze(0) for key, val in inputs.items()}