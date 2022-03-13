# services/logs.py
# setting up custom logging

import logging


def logging_setup() -> logging.Logger:
    """
    logging_setup
    
    Returns a configured logger for the application

    """
    logging.basicConfig(
        format="{levelname:7} {message}", style="{", level=logging.DEBUG
    )

    logger = logging.getLogger("my-application")

    return logger


logger = logging_setup()
