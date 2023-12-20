from random import randint
from threading import Thread, Barrier
from time import sleep, ctime
import logging


def worker(barrier_: Barrier):
    logging.debug(f'started at: {ctime()}')
    sleep(randint(1, 3))
    r = barrier_.wait()
    logging.debug(f'count: {r}')
    sleep(0.2)
    logging.debug(f'barrier overcome at: {ctime()}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    barrier = Barrier(5)

    for i in range(10):
        thread = Thread(name=f'Thread-{i}', target=worker, args=(barrier,))
        thread.start()
