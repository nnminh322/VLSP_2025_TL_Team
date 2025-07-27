# -*- coding: utf-8 -*-
import torch
from torch.utils.data import DataLoader

def train_reranker_epoch(model, dataloader: DataLoader, optimizer: torch.optim.Optimizer, loss_fn, device: str):
    """
    Mục đích:
        Thực hiện một epoch training cho model reranker.

    Trả về:
        float: Giá trị loss trung bình của epoch.

    Logic chính:
        1. Đặt model vào chế độ training (`model.train()`).
        2. Lặp qua từng batch trong `dataloader`.
        3. Chuyển batch dữ liệu và labels sang `device`.
        4. Đưa batch qua model để lấy ra logits (điểm số thô).
        5. Tính toán loss bằng `loss_fn` (ví dụ: BCEWithLogitsLoss) giữa logits và labels.
        6. Thực hiện backpropagation và cập nhật trọng số.
    """
    model.train()
    total_loss = 0
    for batch in dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}
        labels = batch.pop('labels')
        
        optimizer.zero_grad()
        outputs = model(**batch)
        logits = outputs.logits
        loss = loss_fn(logits.squeeze(), labels)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        
    return total_loss / len(dataloader)