import logging
from logging.handlers import TimedRotatingFileHandler
import time


def main():
    logging.basicConfig(level=logging.INFO)

    handler = TimedRotatingFileHandler('timed_log.log', when='midnight', interval=15, backupCount=7, encoding='utf-8')

    logger = logging.getLogger()
    logger.addHandler(handler)

    for i in range(100000):
        logger.info(i)
        logger.info("У попа була собака, він її любив")
        logger.error("Вона з'їла кусок м'яса, він її убив")
        time.sleep(4)


if __name__ == '__main__':
    main()
