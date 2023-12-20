from threading import Timer
from time import sleep
import logging


def example_work():
    logging.debug('Start')
    sleep(0.5)
    logging.debug('End function')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    first = Timer(0.5, example_work)
    first.name = 'FirstThread'
    second = Timer(0.7, example_work)
    second.name = 'SecondThread'
    logging.debug('Start timers')
    first.start()
    second.start()
    sleep(0.6)
    second.cancel()
    logging.debug('End program')
