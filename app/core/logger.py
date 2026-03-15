from loguru import logger
import sys

def setup_logger():
    """
    Configure Application Logging
    """

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        format="{time} | {level} | {message}",
)
    
    logger.add("app.log", rotation="10 MB")

    return logger


