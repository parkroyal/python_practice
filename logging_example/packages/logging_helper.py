import logging
from datetime import date
import os

log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# set logger name: if import 
logger = logging.getLogger(__name__)
# setting level 
logger.setLevel(logging.DEBUG)
# setting log format  
formatter = logging.Formatter('%(asctime)s - %(name)s- %(filename)s- %(levelname)s - %(funcName)s: %(message)s')
# write data to x.log
file_name = os.path.join(log_folder, f'{date.today()}.log')
file_handler = logging.FileHandler(file_name)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_formatter = logging.Formatter('%(levelname)s - %(funcName)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)