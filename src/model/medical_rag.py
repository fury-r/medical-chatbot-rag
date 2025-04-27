from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA  # RAG
from src.helper.prompt import prompt_template as default_prompt_template
from src.helper.logger import logging
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

class MedicalRAG:
    """Class representing a rag config"""

    def __init__(
            self,
            model_path,
            model_type,
            config,
            retriever,
            k=0,
            prompt_template=default_prompt_template):
        logging.log(
            logging.INFO,
            "creating RAG with model {model_path} and type {model_type}")
        self.llm = CTransformers(
            model=model_path,
            model_type=model_type,
            config=config)
        self.qa = None
        if k > 1:
            self.create_rag_with_memory(retriever, prompt_template, k)
        else:
            self.create_rag(retriever, prompt_template)

    def create_rag(self, retriever, prompt_template):
        logging.log(logging.INFO, "creating rag without memory")
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": prompt_template})

    def create_rag_with_memory(self, retriever, prompt_template, k):
        logging.log(logging.INFO, f"creating rag with :{k}")
        if k == 0:
            memory = ConversationBufferMemory(
                memory_key="chat_history", return_messages=True)
        else:
            memory = ConversationBufferWindowMemory(
                memory_key="chat_history", k=k, return_messages=True)
        self.qa = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={
                "prompt": prompt_template})

    def query(self, user_query):
        if isinstance(self.qa, ConversationalRetrievalChain):
            result = self.qa({"question": user_query, "output_key": "answer"})
            logging.log(logging.INFO, f"response from memory rag: {result}")
            return result["answer"]
        return self.qa({"query": user_query})
