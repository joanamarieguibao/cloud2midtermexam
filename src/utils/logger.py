import logging
import os


def create_logger(log_file="logs/app.log"):

    folder = os.path.dirname(log_file)

    if folder:
        os.makedirs(folder, exist_ok=True)

    logger = logging.getLogger("StudentSystem")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger