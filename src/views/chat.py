from src import app
from flask import render_template, request
from src import rag_qa
import logging


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/v1/get-answer", methods=["POST"])
def get_answer():
    msg = request.get_json()
    logging.log(logging.INFO, f"user query:{msg}")

    try:
        input_query = msg['text']
        result = rag_qa.query(input_query)

        logging.log(logging.INFO, f"raw response for model:{result}")
        return str(result["result"])
    except Exception as e:
        logging.log(logging.ERROR, f"error occured: {e}", stack_info=True)
        return "Error occurred", 500
