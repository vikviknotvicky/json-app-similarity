from datetime import datetime
import logging
import sys


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
        logging.FileHandler(f"logs/qb-app-{datetime.today().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()
    ]
)
