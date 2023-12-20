from threading import Thread, RLock
from time import time, sleep
import logging


def func(locker, delay):
    timer = time()
    locker.acquire()
    logging.debug('acquired')
    sleep(delay)
    locker.release()
    logging.debug('released')
    logging.debug(f'Done in {time() - timer} seconds')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    lock = RLock()
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))
    logging.debug('Started')
    t1.start()
    t2.start()
    logging.debug('Ended')
