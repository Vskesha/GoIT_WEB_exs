import time
from functools import wraps


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper


@timelogger
def long_loop(num: int):
    """
    Long loop

    :param num:
    :return: None
    """
    while num > 0:
        num -= 1


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("decorator1")
        return result
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("decorator2")
        return result
    return wrapper


@decorator1
@decorator2
def baz(name):
    return f'Hello {name}'


if __name__ == '__main__':
    # long_loop(1_000_000)
    # print(long_loop.__name__)
    # print(long_loop.__doc__)
    # print(long_loop.__annotations__)
    print(baz('Edward'))
    print(baz.__wrapped__('Oleksandr'))
    print(baz.__wrapped__.__wrapped__('Evgeny'))
