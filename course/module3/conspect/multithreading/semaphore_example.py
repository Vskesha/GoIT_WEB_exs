from threading import Thread, Semaphore
from time import sleep
import random
import logging


def worker(condition):
    with condition:
        logging.debug('got semaphore')
        r = round(random.random() * 3, 1)
        logging.debug(f'will be for {r} seconds')
        sleep(r)
        logging.debug('finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    pool = Semaphore(2)
    for n in range(10):
        thread = Thread(name=f'Thread-{n}', target=worker, args=(pool,))
        thread.start()
