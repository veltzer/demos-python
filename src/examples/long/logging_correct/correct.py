import logging


def bar():
    logger = logging.getLogger(__name__)
    logger.info("in bar")
