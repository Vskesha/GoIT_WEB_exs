from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import random
import logging


def greeting(name: str):
    logging.debug(f'greeting for: {name}')
    sleep(random() * 4)
    return f'Hello, {name}!'


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(greeting, arguments)

    for result in results:
        logging.debug(result)
