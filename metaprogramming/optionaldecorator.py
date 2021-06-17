from functools import partial, wraps
import logging


def logged(func=None, level=logging.ERROR, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__name__
    log = logging.getLogger(logname)
    log_msg = message if message else func.__module__

    def wrapper(*args, **kwargs):
        logging.log(level, log_msg)
        return func(*args, **kwargs)
    return wrapper


@logged(level=logging.CRITICAL, name='add', message='add x and y')
def add(x, y):
    return x + y

if __name__ == '__main__':
    add(1, 2)