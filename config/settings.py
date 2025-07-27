# -*- coding: utf-8 -*-
"""
Mục đích:
    Tệp này chứa tất cả các biến cấu hình cho dự án.
    Việc tập trung cấu hình tại một nơi giúp dễ dàng quản lý và thay đổi
    các tham số mà không cần can thiệp vào code logic.
"""
# --- Đường dẫn ---
DATA_DIR = "data/processed_data/"
RAW_DATA_DIR = "data/raw_data/" # Thêm đường dẫn dữ liệu thô
EVALUATION_DATA_PATH = "data/evaluation_set.json"
QH15_ARTICLES_PATH = f"{DATA_DIR}qh15_articles.json"
QCVN41_ARTICLES_PATH = f"{DATA_DIR}qcvn41_articles.json"
VECTOR_STORE_PATH = "vector_database/db.faiss"
MODEL_SAVE_DIR = "models/saved_models/"

# --- Cấu hình Model ---
ENCODER_MODEL_NAME = "vinai/vinai-clip-vit-b-16"
RERANKER_MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# --- Cấu hình Vector Database ---
VECTOR_DIMENSION = 512 # vinai-clip-vit-b-16 có dim 512
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
QDRANT_COLLECTION_NAME = "traffic_law_vn"

# --- Cấu hình Retrieval ---
TOP_K_RETRIEVAL = 50 # Số lượng văn bản lấy ra từ vector store
TOP_K_RERANK = 5   # Số lượng văn bản cuối cùng trả về sau khi rerank

# --- Cấu hình Training ---
BATCH_SIZE = 32
LEARNING_RATE = 2e-5
NUM_EPOCHS = 3