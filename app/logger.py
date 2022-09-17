import logging

from app.config import settings
import sys


class Logger:
    """Class to manage logger service."""

    def get_logger(name='muntants', level=None, log_path=None):
        """Retrieves logger module."""

        try:
            if log_path is None:
                log_path = settings.PATCH_LOGS
            logger = logging.getLogger(name)
            log_format = '%(asctime)s - %(levelname)s - %(pathname)s - Line: %(lineno)d - '
            formatter = logging.Formatter(fmt=log_format + " %(message)s")
            file_handler = logging.FileHandler(log_path + '/' + name + ".log")
            file_handler.setFormatter(formatter)
            handler = logging.StreamHandler(sys.stdout)
            logger.handlers = []
            logger.addHandler(file_handler)
            logger.addHandler(handler)
            if level is None:
                level = settings.LEVEL_LOGS
            logger.setLevel(level)
            logger.propagate = False
            return logger
        except Exception as ex:
            raise ex
