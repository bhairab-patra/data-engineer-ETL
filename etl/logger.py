import logging
import os

def get_logger(name):
    
    logger = logging.getLogger(name)
    
    
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(message)s'
    )

    # File handler — logs folder mein save ho
    os.makedirs('logs', exist_ok=True)
    file_handler = logging.FileHandler('logs/etl.log')
    file_handler.setFormatter(formatter)

    # Terminal handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger