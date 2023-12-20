from threading import Thread, Barrier, RLock, current_thread
from time import sleep, ctime
from random import randint
import logging


def worker(barrier_: Barrier):
    name = current_thread().name
    logging.info(f'Start thread: {name} at {ctime()}')
    num = barrier_.wait()
    sleep(randint(1, 3))
    logging.info(f'Barrier overcome: {name}#{num} at {ctime()}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    barrier = Barrier(4)

    for i in range(12):
        w = Thread(target=worker, args=(barrier,))
        w.start()

    logging.info('End program')
