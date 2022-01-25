import logging
import sys
# print(sys.path())
logging.basicConfig(filename='test1.log',level=logging.DEBUG,format='%(asctime)s - %(filename)s- %(levelname)s - %(funcName)s: %(message)s')

def add(a,b):
    try:
        return logging.debug(f'{a+b}')
    except TypeError:
        return logging.error(f'a:{type(a)}')


def main():
    # print(sys.path())
    add(1,3)
    add(1,'3')  
# try:
#     logging.raiseExceptions('')

if __name__ == '__main__':
    main()