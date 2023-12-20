from multiprocessing import Process, Queue
from time import sleep
from random import randint
import logging
import sys


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

q = Queue()


def worker(queue: Queue):
    logger.debug('started')
    sleep(0.2)
    while True:
        val = queue.get()
        if val is None:
            break
        logger.debug(val ** 2)
        sleep(randint(5, 35) / 10)
    logger.debug('finished')
    sys.exit(0)


if __name__ == '__main__':
    r = randint(3, 25)
    print('Total processes: ', r)
    sleep(2)
    processes = []
    for i in range(r):
        pr = Process(name=f'Proces-{i}', target=worker, args=(q,))
        pr.start()
        processes.append(pr)

    for _ in range(50):
        q.put(randint(3, 12))

    for _ in processes:
        q.put(None)
    [pr.join() for pr in processes]
    [print(pr.exitcode, end=' ') for pr in processes]