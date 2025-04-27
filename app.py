
from src import app
from src.helper.logger import logging
if __name__=="__main__":
    logging.log(logging.INFO,"starting app...")
    app.run("0.0.0.0",8080,debug=True,)