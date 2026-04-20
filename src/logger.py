import logging
import os
from datetime import datetime

# ── anchor to THIS file's location ──────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))        # .../MlProject/src
PROJECT_ROOT = os.path.dirname(BASE_DIR)                     # .../MlProject

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y')}.log"

logs_path = os.path.join(PROJECT_ROOT, "logs")               # always MlProject/logs/
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)            # MlProject/logs/04_20_26....log

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")