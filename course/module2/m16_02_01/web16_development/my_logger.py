import logging

log_format = ("[%(levelname)s] %(asctime)s: %(name)s module: %(module)s; "
              "func: %(funcName)s; line: %(lineno)d - %(message)s")

file_handler = logging.FileHandler("application.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(log_format))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name, level):
    logger_ = logging.getLogger(name)
    logger_.setLevel(level)
    logger_.addHandler(file_handler)
    logger_.addHandler(stream_handler)

    return logger_


logger = get_logger("my_logger", logging.DEBUG)

if __name__ == '__main__':
    pass
