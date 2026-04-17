import logging

from pythonjsonlogger import jsonlogger


def get_logger(name: str = "ml_app"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")

        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)

    return logger
