from threading import Thread, Event
from time import sleep
import logging


def worker(event):
    logging.debug('ready to work')
    event.wait()
    logging.debug('doing his work')


def master(event):
    logging.debug('is doing some work')
    sleep(2)
    logging.debug('informs that workers can do their work')
    event.set()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event_ = Event()
    master = Thread(name='master', target=master, args=(event_,))
    worker_one = Thread(name='worker_one', target=worker, args=(event_,))
    worker_two = Thread(name='worker_two', target=worker, args=(event_,))
    worker_one.start()
    worker_two.start()
    master.start()
    worker_one.join()
    worker_two.join()
    master.join()
    logging.debug('End program')
