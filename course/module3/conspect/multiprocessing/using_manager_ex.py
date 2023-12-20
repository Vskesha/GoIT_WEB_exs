from multiprocessing import Process, Manager, current_process
from random import randint
from time import sleep
import logging

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(delay, val: Manager):
    name = current_process().name
    logger.debug(f'Started {name}')
    sleep(delay)
    val[name] = current_process().pid
    logger.debug(f'Done {name}')


if __name__ == '__main__':
    with Manager() as manager:
        m = manager.dict()
        processes = []
        for i in range(5):
            pr = Process(name=f'Pr{i+1}', target=worker, args=(randint(1, 3), m))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(m)
