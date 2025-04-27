


from dotenv import load_dotenv
import os
from src.helper.logger import logging
load_dotenv()

class Config:
    def __init__(self):
        logging.log(logging.INFO,"loading configs for environment")
        self.huggingface_api_token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_env = os.getenv("PINECONE_ENV")
        self.pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
        self.hugging_face_model_name = os.getenv("HUGGING_FACE_MODEL_NAME")
        self.model_path = os.getenv("MODEL_PATH")
        self.model_type = os.getenv("MODEL_TYPE")
        self.model_token_limit=int(os.getenv("MODEL_TOKEN_LIMIT") if os.getenv("MODEL_TOKEN_LIMIT") else "512")        
        self.model_temperature=float(os.getenv("MODEL_TEMPERATURE") if os.getenv("MODEL_TEMPERATURE") else "0.8")
        self.model_memory= int(os.getenv("MODEL_MEMORY") if os.getenv("MODEL_MEMORY") else "0")    