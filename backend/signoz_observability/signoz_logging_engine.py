import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("signoz_logger")

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
