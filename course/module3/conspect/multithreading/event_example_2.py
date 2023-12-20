from threading import Thread, Event
from time import sleep
import logging


def example_work(event_for_exit: Event):
    i = 1
    while True:
        logging.debug(f'{i}-th iteration of example_work')
        sleep(1)
        i += 1
        if event_for_exit.is_set():
            break


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    event = Event()
    thread = Thread(target=example_work, args=(event,))
    thread.start()
    sleep(5)
    event.set()
    logging.debug('End program')
