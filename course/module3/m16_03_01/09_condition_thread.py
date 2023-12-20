from threading import Condition, Thread
from time import sleep
import logging


def master(con: Condition):
    logging.info('Master work hard')
    sleep(1)
    with con:
        logging.info("It's time to do something...")
        con.notify_all()


def worker(con: Condition):
    logging.info('Waiting for master order')
    with con:
        con.wait()
        logging.info('Workers work hard')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    con = Condition()

    m = Thread(target=master, args=(con,))
    w1 = Thread(target=worker, args=(con,))
    w2 = Thread(target=worker, args=(con,))

    w1.start()
    w2.start()
    m.start()
    
    logging.info('End program')