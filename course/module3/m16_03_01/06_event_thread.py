from threading import Thread, Event, current_thread
from time import sleep
import logging


def worker_smart(event: Event, time: float):
    while not event.is_set():
        logging.info('Waiting for event set to complete')
        e_wait = event.wait(time)
        if e_wait:
            logging.info('Doing work because master set event')
        else:
            logging.info('We can play games')


def worker_stupid(event: Event):
    logging.info(f'{current_thread().name} is waiting')
    event.wait()
    logging.info(f'{current_thread().name} is working')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()

    wrk = Thread(target=worker_stupid, args=(event,))
    wrk.start()

    smart = Thread(target=worker_smart, args=(event, 1))
    smart.start()

    sleep(3)
    event.set()
    logging.info('End program')
