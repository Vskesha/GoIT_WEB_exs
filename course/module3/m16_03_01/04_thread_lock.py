from threading import Thread, RLock
from time import sleep
from random import randint
import logging

counter = 0
lock = RLock()


def worker():
    global counter
    while True:
        # lock.acquire()
        sleep(randint(1, 3))
        with lock:
            counter += 1
            with open('result.txt', 'a') as fd:
                fd.write(f'{counter}\n')
        # lock.release()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.info('Start program')

    for i in range(5):
        th = Thread(target=worker, name=f'Thread#{i + 1}')
        th.start()

    logging.info('End program')
