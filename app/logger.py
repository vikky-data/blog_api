import logging 
from app.core.config import  settings 


def create_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging,settings.LOG_LEVEL))

    if not logger.handlers: 
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(settings.LOG_FILE)

        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s") 

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger 


