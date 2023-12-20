from random import randint
from threading import Thread
from time import sleep
import logging


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.args = args

    def run(self):
        ttl = randint(1, 3)
        sleep(ttl)
        logging.info(f"In my threat {self.name}: {ttl} seconds")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    threads = []
    for i in range(5):
        th = MyThread(name=f'MyThread#{i + 1}', args=(f'Count th- {i}',), daemon=True)
        th.start()
        threads.append(th)

    sleep(2)
    # [th.join() for th in threads]
    logging.info('End program')
