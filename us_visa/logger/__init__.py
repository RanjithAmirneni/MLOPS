import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
logger_folder_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(os.path.dirname(logger_folder_path))

final_logs_path = os.path.join(root_path, log_dir, LOG_FILE)

final_logs_dir = os.path.join(root_path, log_dir)
os.makedirs(final_logs_dir, exist_ok=True)

logging.basicConfig(
    filename=final_logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",level=logging.DEBUG,)
