from multiprocessing import Process, RLock, current_process
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
import logging


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(num: Value, string: Array, arr: Array):
    logger.debug(f'Started {current_process().name}')

    logger.debug(f'Change num: {num.value}')
    with num.get_lock():
        num.value **= 2
    logger.debug(f'to num: {num.value}')

    with string.get_lock():
        string.value = string.value.upper()

    with arr.get_lock():
        for a in arr:
            a.x **= 2
            a.y **= 2

    logger.debug(f'Done {current_process().name}')


if __name__ == '__main__':
    lock = RLock()
    number = Value(c_double, 1.5, lock=lock)
    string = Array('c', b'hello world', lock=lock)
    array = Array(Point, [(1, -6), (-5, 2), (2, 9)], lock=lock)

    p1 = Process(name='Pr1', target=modify, args=(number, string, array))
    p2 = Process(name='Pr1', target=modify, args=(number, string, array))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(number.value)
    print(string.value)
    print([(p.x, p.y) for p in array])
