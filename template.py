import os
from pathlib import Path

import logging


logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s:")


list_of_tasks=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "experiment/chatbot.ipynb",
    "app.py",
    "store_index.py",
    "templates/chat.html",
    ]

for path in list_of_tasks:
    filepath=Path(path)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir}")

    if (not os.path.exists(filepath) ) :
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating file: {filepath}")
    else:
        logging.info(f"file already exists: {filename}")
