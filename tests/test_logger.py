import logging
import os
from config.logs.logger_config import setup_logger


def remove_log_file_handler(logger, log_file):
    """Closes log file handler."""
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.close()
            logger.removeHandler(handler)


def test_logger_file_creation():
    """Checks if the log file is created after the logger is configured."""
    log_file = 'test_log.log'

    if os.path.exists(log_file):
        os.remove(log_file)

    logger = setup_logger(log_file)

    assert os.path.exists(log_file), "Logs file was not created."

    remove_log_file_handler(logger, log_file)

    os.remove(log_file)


def test_logger_writes_to_file():
    """Checks if the logger correctly writes to the log file."""
    log_file = 'test_log.log'

    if os.path.exists(log_file):
        os.remove(log_file)

    logger = setup_logger(log_file)

    logger.info("Log test message")

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert "Log test message" in log_content, "The log message was not written to the file."

    remove_log_file_handler(logger, log_file)

    os.remove(log_file)
