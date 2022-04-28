from packages.logging_helper import logger

def multiply(x:int, y:int):
    """Multiply Function"""
    return x * y


def divide(a:int, b:int):
    """Divide Function"""
    try:
        result = a / b
        logger.debug(f'{result}')
    except TypeError:
        return logger.error(f'a: {type(a)}, b: {type(b)}')
    except Exception:
        return logger.exception(f'other errors happened.')
    else:
        return logger.info(f'succuessfully return.')
