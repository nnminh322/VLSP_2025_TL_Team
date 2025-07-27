# -*- coding: utf-8 -*-
from typing import List, Dict, Any
from torch.utils.data import Dataset

class RerankerDataset(Dataset):
    """
    Mục đích:
        Tạo một đối tượng Dataset của PyTorch để cung cấp dữ liệu cho việc
        training model Reranker (Cross-Encoder). Dataset này hoạt động dựa trên
        các cặp (query, document) và một nhãn (label) cho biết chúng có liên quan không.
    """
    def __init__(self, data: List[Dict[str, Any]], tokenizer):
        """
        Tham số:
            data (List[Dict[str, Any]]): Danh sách dữ liệu. Mỗi phần tử là một dict
                                         chứa 'query', 'document' và 'label'.
            tokenizer: Tokenizer của model Cross-Encoder.
        """
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        """
        Mục đích:
            Lấy một mẫu dữ liệu tại vị trí `idx` và tokenize nó.

        Trả về:
            Dict[str, Any]: Một dictionary chứa `input_ids`, `attention_mask`, và `labels`
                            đã được xử lý cho model.

        Logic chính:
            1. Lấy cặp query, document và label tại `self.data[idx]`.
            2. Sử dụng `self.tokenizer` để tokenize cặp (query, document) cùng lúc.
            3. Thêm nhãn (label) vào kết quả.
        """
        item = self.data[idx]
        query = item['query']
        document = item['document']
        label = item['label']
        
        # Tokenizer cho cross-encoder xử lý cặp câu
        inputs = self.tokenizer(query, document, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
        inputs = {key: val.squeeze(0) for key, val in inputs.items()}
        inputs['labels'] = torch.tensor(label, dtype=torch.float)
        return inputs