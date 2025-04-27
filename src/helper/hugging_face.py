
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.helper.logger import logging


def download_hugging_face_embedding(model_name):
    logging.log(
        logging.INFO,
        f"downloading embeddings for model: {model_name}")
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings
