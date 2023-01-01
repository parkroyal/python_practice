import logging

# logging.basicConfig(filename='log_from_multiple.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s- %(filename)s- %(levelname)s - %(funcName)s: %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s- %(filename)s- %(levelname)s - %(funcName)s: %(message)s')

file_handler = logging.FileHandler('log_from_multiple.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def multiply(x:int, y:int):
    """Multiply Function"""
    return x * y

def main(a, b):
    # logging.info('Start Script')
    logger.info('Start Script')
    multiply(a, b)

main(a = 3, b = 3)