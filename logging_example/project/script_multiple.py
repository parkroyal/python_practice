from packages.math import multiply 
from packages.logging_helper import logger

def main(a, b):
    logger.info('Start Script')
    multiply(a, b)

if __name__ == '__main__':
    main(3, 0)