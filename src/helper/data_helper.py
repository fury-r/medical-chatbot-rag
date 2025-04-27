
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import  RecursiveCharacterTextSplitter
from src.helper.logger import logging

def load_pdf(path):
    logging.log(logging.INFO,f"loading pdf with path: {path}")
    loader=DirectoryLoader(path,glob="*.pdf",loader_cls=PyPDFLoader)
    docs=loader.load()
    return docs


def create_chunks(data):
    logging.log(logging.INFO,f"creating chunks for documents: length-{len(data)}")
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks=text_splitter.split_documents(data)
    return text_chunks