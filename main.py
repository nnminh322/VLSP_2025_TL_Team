# -*- coding: utf-8 -*-
import config.settings as settings
from utils.image_processing import load_image
from data.load_data import load_documents
from models.representation.multimodal_encoder import MultimodalEncoder
from models.reranker.cross_encoder import Reranker
from vector_database.faiss_vector_store import FaissVectorStore
from retrieval.multimodal_retriever import MultimodalRetriever

def main():
    """
    Mục đích:
        Hàm chính để chạy một ví dụ hoàn chỉnh của hệ thống RAG.
        Hàm này sẽ mô phỏng một yêu cầu từ người dùng và in ra kết quả.
    """
    # 1. Tải và chuẩn bị dữ liệu (Bước này thường chỉ làm 1 lần và lưu lại)
    #    - `all_docs = load_documents(...)`
    #    - `processed_docs = preprocess_documents(all_docs)`
    #    - Tạo embeddings cho `processed_docs` và lưu vào FAISS.
    #    - Ở đây, ta giả sử đã có sẵn file index.

    print("--- Khởi tạo hệ thống Multimodal RAG ---")
    # 2. Khởi tạo các thành phần của hệ thống
    all_docs = load_documents(settings.QH15_ARTICLES_PATH) # Ví dụ
    
    encoder = MultimodalEncoder(model_name=settings.ENCODER_MODEL_NAME)
    reranker = Reranker(model_name=settings.RERANKER_MODEL_NAME)

    vector_store = FaissVectorStore(dimension=settings.VECTOR_DIMENSION)
    vector_store.load(settings.VECTOR_STORE_PATH)

    retriever = MultimodalRetriever(
        encoder=encoder,
        reranker=reranker,
        vector_store=vector_store,
        all_documents=all_docs
    )
    print("--- Hệ thống đã sẵn sàng ---")

    # 3. Mô phỏng một query từ người dùng
    query_text = "Biển báo này có ý nghĩa gì và vi phạm sẽ bị phạt bao nhiêu?"
    query_image_path = "path/to/your/traffic_sign_image.jpg"
    query_image = load_image(query_image_path)

    print(f"\nCâu hỏi: {query_text}")
    print(f"Ảnh: {query_image_path}")

    # 4. Thực hiện retrieval
    results = retriever.retrieve(
        query_text=query_text,
        query_image=query_image,
        top_k_retrieval=settings.TOP_K_RETRIEVAL,
        top_k_rerank=settings.TOP_K_RERANK
    )

    # 5. In kết quả
    print("\n--- Các điều luật liên quan nhất được tìm thấy: ---")
    if not results:
        print("Không tìm thấy kết quả phù hợp.")
    else:
        for i, doc in enumerate(results):
            print(f"\nKết quả {i+1}:")
            print(f"  ID: {doc.get('id', 'N/A')}")
            print(f"  Nội dung: {doc['text'][:300]}...") # In 300 ký tự đầu

if __name__ == "__main__":
    main()