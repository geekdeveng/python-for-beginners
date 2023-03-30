"""
-author : geekdev
-desc : utils
"""

import logging, os, datetime, json
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)

def set_logger() -> None:
    """
    -desc   : Must be called once to use
    -param  : None
    -return : None
    """
    
    LOG_DIR: str = "logs"

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger.setLevel(logging.DEBUG)
    logger.propagate = True
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] " + 
        "[filename:%(filename)s, lineno:%(lineno)s, funcName:%(funcName)s()] %(message)s", 
        "%Y-%m-%d %H:%M:%S"
    )
    streamHandler = logging.StreamHandler()
    fileHandler = TimedRotatingFileHandler(
        filename=LOG_DIR + '/log.log', 
        when = "midnight",
        backupCount= 30, 
        atTime=datetime.time(0, 0, 0)
    )
    fileHandler.setLevel(logging.DEBUG)
    streamHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
