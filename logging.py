import logging
import os


def init_logger(logging_name='scraping'):

    logger = logging.getLogger(logging_name)
    logger.setLevel(logging.INFO)

    try:
        os.makedirs('log', exist_ok=True)
    except Exception as e:
        print(e)

    # create a file handler
    handler = logging.FileHandler(f'log/{logging_name}.log')
    handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(stream_handler)

    return logger
