import os
from src.views import chat
from dotenv import load_dotenv
from flask import Flask
from src.db.store_index import Pinecone
from src.helper.config import Config
from src.model.medical_rag import MedicalRAG
from src.helper.data_helper import create_chunks, load_pdf
from src.helper.hugging_face import download_hugging_face_embedding
from src.helper.logger import initLogger

initLogger()

template_dir = os.path.join(os.getcwd(), 'src', 'templates')
static_dir = os.path.join(os.getcwd(), 'src', 'static')
app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir,
    static_url_path='/static'
)

load_dotenv()

config = Config()

docs = load_pdf("./data")
text_chunks = create_chunks(docs)
embedding = download_hugging_face_embedding(config.hugging_face_model_name)

pinecone_client = Pinecone(
    config.pinecone_api_key,
    config.pinecone_env,
    config.pinecone_index_name
)

pinecone_client.add_to_vectordb(
    [t.page_content for t in text_chunks],
    embedding, config.pinecone_index_name
)

rag_qa = MedicalRAG(
    model_path=config.model_path,
    model_type=config.model_type,
    k=config.model_memory,
    config={
        "max_new_tokens": config.model_token_limit,
        "temperature": config.model_temperature
    },
    retriever=pinecone_client.vectordb
    .as_retriever(
        search_kwargs={
            "k": 2
        }
    )
)
