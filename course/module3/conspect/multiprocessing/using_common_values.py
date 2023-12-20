from multiprocessing import Process, Value, RLock, current_process
from time import sleep
import logging
import sys


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def workrer(val: Value):
    logger.debug(f'Started {current_process().name}')
    sleep(2)
    with val.get_lock():
        val.value -= 1
    logger.debug(f'Done {current_process().name}')
    sys.exit(0)


if __name__ == '__main__':
    lock = RLock()
    value = Value('l', 0, lock=lock)
    print(value.value)
    pr1 = Process(name='Pr1', target=workrer, args=(value,))
    pr1.start()
    pr2 = Process(name='Pr2', target=workrer, args=(value,))
    pr2.start()
    pr1.join()
    pr2.join()
    print(value.value)