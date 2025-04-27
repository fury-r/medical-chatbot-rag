from langchain_pinecone import PineconeVectorStore
from src.helper.logger import logging
from pinecone import Pinecone as PineconeClient


class Pinecone:
    def __init__(self, api_key, env, index_name=None):
        logging.log(logging.INFO, "Initializing Pinecone client")

        self.__api_key = api_key
        self.__env = env
        self.client=PineconeClient(api_key=self.__api_key, environment=self.__env)  

        self.__index_name = None
        self.index = None
        self.vectordb = None
        if not index_name:
            self.set_index(index_name)
            self.clear_vectordb()

    def add_to_vectordb(self, content, embedding, index_name=None):
        logging.log(logging.INFO, "Adding text data to vectordb by converting text data embeddings")

        if index_name:
            self.set_index(index_name)
        
        logging.log(logging.INFO, f"indexes: {self.client.list_indexes()}")

        self.vectordb = PineconeVectorStore.from_texts(
            content,
            embedding=embedding,
            index_name=self.__index_name,
        )
    
    def clear_vectordb(self):
        self.vectordb.delete(None,True)

    def set_index(self, index_name):
        logging.log(logging.INFO, f"Update index_name: {index_name}")
        self.__index_name = index_name
        self.index = self.client.Index(index_name) 
        self.index.delete(delete_all=True)
        logging.log(logging.INFO, f"Updated index")
