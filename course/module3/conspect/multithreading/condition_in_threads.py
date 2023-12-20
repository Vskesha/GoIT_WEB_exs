from threading import Thread, Condition
from time import sleep
import logging


def worker(condition):
    logging.debug('ready to work')
    with condition:
        condition.wait()
        logging.debug('doing his work')


def master(condition):
    logging.debug('is doing some work')
    sleep(2)
    with condition:
        logging.debug('informs that workers can do their work')
        condition.notify_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    condition = Condition()
    master = Thread(name='master', target=master, args=(condition,))
    worker_one = Thread(name='worker_one', target=worker, args=(condition,))
    worker_two = Thread(name='worker_two', target=worker, args=(condition,))
    worker_one.start()
    worker_two.start()
    master.start()
    worker_one.join()
    worker_two.join()
    master.join()
    logging.debug('End program')
