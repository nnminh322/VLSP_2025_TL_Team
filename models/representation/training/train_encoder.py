# -*- coding: utf-8 -*-
import torch
from torch.utils.data import DataLoader

def train_encoder_epoch(model, dataloader: DataLoader, optimizer: torch.optim.Optimizer, device: str):
    """
    Mục đích:
        Thực hiện một epoch training cho model encoder.

    Tham số:
        model: Model encoder cần train (đã được chuyển sang device).
        dataloader (DataLoader): DataLoader cung cấp các batch dữ liệu.
        optimizer (torch.optim.Optimizer): Optimizer để cập nhật trọng số.
        device (str): Thiết bị ('cpu' hoặc 'cuda') để thực hiện tính toán.

    Trả về:
        float: Giá trị loss trung bình của epoch.

    Logic chính:
        1. Đặt model vào chế độ training (`model.train()`).
        2. Lặp qua từng batch trong `dataloader`.
        3. Chuyển batch dữ liệu sang `device`.
        4. Đưa batch qua model để lấy output. Đối với CLIP, output chứa `loss`.
        5. Lấy giá trị loss từ output.
        6. Thực hiện backpropagation: `loss.backward()`.
        7. Cập nhật trọng số: `optimizer.step()`.
        8. Xóa gradient: `optimizer.zero_grad()`.
        9. Tính tổng loss để trả về loss trung bình cuối epoch.
    """
    model.train()
    total_loss = 0
    for batch in dataloader:
        # Chuyển batch tới device
        batch = {k: v.to(device) for k, v in batch.items()}
        
        optimizer.zero_grad()
        outputs = model(**batch, return_loss=True)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        
    return total_loss / len(dataloader)