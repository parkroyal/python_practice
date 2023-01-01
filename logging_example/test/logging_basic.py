import logging
import multiple


logging.basicConfig(filename='log.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s- %(filename)s- %(levelname)s - %(funcName)s: %(message)s')

# def divide(a:int, b:int):
#     try:
#         result = a / b
#         logging.debug(f'{result}')
#     except TypeError:
#         return logging.error(f'a: {type(a)}, b: {type(b)}')
#     else:
#         return logging.info(f'succuessfully return.')

def divide(a:int, b:int):
    try:
        result = a / b
        logging.debug(f'{result}')
    except TypeError:
        return logging.error(f'a: {type(a)}, b: {type(b)}')
    except Exception:
        return logging.exception(f'other errors happened.')
    else:
        return logging.info(f'succuessfully return.')

def main():
    divide(1,3)
    divide(1,'3')     # -> 數字與字串
    divide(1, 0)      # -> 分母為0

if __name__ == '__main__':
    main()