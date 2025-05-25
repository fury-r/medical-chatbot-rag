from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from src.helper.prompt import prompt_template as default_prompt_template
from src.helper.logger import logging
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

class MedicalRAG:
    """Class representing a RAG config"""

    def __init__(
        self,
        model_path,
        model_type,
        config,
        retriever,
        k=0,
        prompt_template=default_prompt_template
    ):
        logging.log(
            logging.INFO,
            f"Creating RAG with model {model_path} and type {model_type}"
        )

        self.llm = CTransformers(
            model=model_path,
            model_type=model_type,
            config=config
        )

        self.qa = None
        if k > 1:
            self.create_rag_with_memory(retriever, prompt_template, k)
        else:
            self.create_rag(retriever, prompt_template)

    def create_rag(self, retriever, prompt_template):
        logging.log(logging.INFO, "Creating RAG without memory")
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt_template},
            output_key="answer"
        )

    def create_rag_with_memory(self, retriever, prompt_template, k):
        logging.log(logging.INFO, f"Creating RAG with memory, k={k}")

        memory = (
            ConversationBufferWindowMemory(memory_key="chat_history", k=k, return_messages=True, output_key="answer")
            if k > 0
            else ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer")
        )

        self.qa = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": prompt_template},
        )

    def query(self, user_query):
        if isinstance(self.qa, ConversationalRetrievalChain):
            result = self.qa({"question": user_query})
            logging.log(logging.INFO, f"Response from memory RAG: {result}")
            return result["answer"]
        result = self.qa({"query": user_query})
        logging.log(logging.INFO, f"Response from non-memory RAG: {result}")
        return result["answer"]
