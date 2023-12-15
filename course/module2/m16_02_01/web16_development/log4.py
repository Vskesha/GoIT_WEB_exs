import logging
from logging.handlers import RotatingFileHandler
import time


def main():

    logging.basicConfig(level=logging.INFO)

    handler = RotatingFileHandler('rotating_log.log', maxBytes=500, backupCount=3, encoding='utf-8')

    logger = logging.getLogger()
    logger.addHandler(handler)

    for i in range(100000):
        logger.info(i)
        logger.info("У попа була собака, він її любив")
        logger.error("Вона з'їла кусок м'яса, він її убив")
        time.sleep(4)


if __name__ == '__main__':
    main()
