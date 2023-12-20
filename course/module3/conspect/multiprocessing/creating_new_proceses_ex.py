from multiprocessing import Process
from time import sleep
import logging


logger = logging.getLogger('vslogger')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(name)s | %(asctime)s | %(processName)s | %(threadName)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logger.debug(*self.args)


def example_word(params):
    sleep(0.5)
    logger.debug(params)


if __name__ == '__main__':
    processes = []
    for i in range(3):
        pr = Process(name=f'function_process_{i}', target=example_word, args=(f"Count process function - {i}", ))
        pr.start()
        processes.append(pr)

    for i in range(2):
        pr = MyProcess(name=f'class_process_{i}', args=(f"Count process class - {i}", ))
        pr.start()
        processes.append(pr)

    [el.join() for el in processes]
    [print(el.exitcode) for el in processes]
    logger.debug('End of program')
