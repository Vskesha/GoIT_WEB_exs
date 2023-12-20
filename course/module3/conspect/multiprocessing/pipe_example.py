from multiprocessing import Pipe, Process
from time import sleep
import logging
import sys


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


recipient1, sender1 = Pipe()
recipient2, sender2 = Pipe()


def worker(pipe: Pipe):
    logger.debug('started')
    val = pipe.recv()
    # logger.handlers[0].formatter = logging.Formatter("%(message)s")
    logger.debug(val ** 2)
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(name='Pr1', target=worker, args=(recipient1, ))
    w2 = Process(name='Pr2', target=worker, args=(recipient2, ))
    w1.start()
    w2.start()
    logger.debug('started')
    sleep(2)
    sender1.send(8)
    sleep(3)
    sender2.send(16)
