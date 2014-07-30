import os
import logging
from time import localtime, strftime, time
_STR_CURTIME = strftime('%Y%m%d_%H%M%S', localtime())

class TestLogger(logging.Logger):
    def __init__(self, name):
        self._stdout_handler = None
        self._file_handler = None
        logging.Logger.__init__(self, name)

    def add_file_handler(self, level=logging.DEBUG):
        logdir = os.path.join(os.path.expanduser('.'), 'log')
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        logfile = os.path.join(logdir, 'test_%s.log' % (_STR_CURTIME))
        fdlr = logging.FileHandler(logfile)
        fdlr.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fdlr.setFormatter(formatter)
        self.addHandler(fdlr)
        self._file_handler = fdlr

    def add_stdout_handler(self, level=logging.INFO):
        sdlr = logging.StreamHandler()
        sdlr.setLevel(logging.INFO)
        self.addHandler(sdlr)
        self.addHandler(sdlr)
        self._stdout_handler = sdlr

    def enable_stdout_debug(self):
        self._stdout_handler.setLevel(logging.DEBUG)

def getLogger(module):
    logger = TestLogger(module)

    logger.add_stdout_handler()
    logger.add_file_handler()

    return logger
