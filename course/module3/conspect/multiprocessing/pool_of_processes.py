from multiprocessing import Pool
import logging


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(processName)s, pid=%(process)d, %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(x):
    logger.debug(f'{x=}')
    return x * x


if __name__ == '__main__':
    with Pool(processes=3) as pool:
        res = pool.map(worker, range(10))
        logger.debug(res)
