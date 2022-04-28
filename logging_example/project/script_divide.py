# from distutils.log import error
from packages.math import divide
from packages.logging_helper import logger

def main(a, b):
    logger.info('Start Script')
    divide(a, b)

if __name__ == '__main__':
    main(2, 3)
    main(3, 0)