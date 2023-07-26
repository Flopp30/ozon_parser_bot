import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

# Logger
logger: Logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler('parser.log', maxBytes=2097152, backupCount=1000)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Dirs
BASE_DIR = Path(__file__).parent.parent
load_dotenv(BASE_DIR / ".env")


# TG
PARSER_LINK = os.getenv("PARSER_LINK")
MAX_ITEMS_PARSED_COUNT = os.getenv("MAX_ITEMS_PARSED_COUNT")
DEFAULT_ITEMS_PARSED_COUNT = os.getenv("DEFAULT_ITEMS_PARSED_COUNT")
