import logging
import os

LOG_PATH = "logs"
os.makedirs(LOG_PATH, exist_ok=True)

log_file = os.path.join(LOG_PATH, "app.log")


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a"   # append mode
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)


def log_warning(message):
    logging.warning(message)


def log_debug(message):
    logging.debug(message)