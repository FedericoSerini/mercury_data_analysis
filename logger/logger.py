import logging
from colorlog import ColoredFormatter


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):
    __metaclass__ = Singleton

    def __init__(self, classname):
        log_level = logging.DEBUG
        log_format = "%(log_color)s%(levelname)-8s%(reset)s | "+classname+" | %(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(log_level)
        formatter = ColoredFormatter(log_format, force_color=True)
        stream = logging.StreamHandler()
        stream.setLevel(log_level)
        stream.setFormatter(formatter)
        self.log = logging.getLogger('pythonConfig')
        self.log.setLevel(log_level)
        self.log.addHandler(stream)

    def get_log(self):
        return self.log

