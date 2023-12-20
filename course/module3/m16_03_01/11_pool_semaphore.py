from threading import Thread, Semaphore, RLock, current_thread
from time import sleep
from random import randint
import logging


class Logger:
    def __init__(self):
        self.active = []
        self.lock = RLock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.info(f'Started thread: {name}. Active threads: {self.active}')

    def make_inactive(self, name):
        with self.lock:
            if name in self.active:
                self.active.remove(name)
                logging.info(f'Stopped thread: {name}. Active threads: {self.active}')


def worker(semaphore: Semaphore, log: Logger):
    logging.info('waiting ...')
    with semaphore:
        name = current_thread().name
        logging.info('got semaphore')
        log.make_active(name)
        sleep(randint(1, 4))
        logging.info('finished operation')
        log.make_inactive(name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    pool = Semaphore(3)
    logger = Logger()

    for i in range(10):
        w = Thread(name=f'Th{i+1}', target=worker, args=(pool, logger))
        w.start()

    logging.info('End program')