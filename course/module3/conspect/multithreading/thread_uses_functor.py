from threading import Thread
from time import sleep
import logging


class UsefulClass:
    def __init__(self, seconds):
        self.delay = seconds

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(2)
    thread = Thread(target=t2, name='V-thread')
    thread.start()
    print('Some stuff')
