import inspect
import logging


class LoggerObj:

    def getLogger(self):

        fi_handler = logging.FileHandler("logfile.log")
        formater = logging.Formatter("%(asctime)s =>%(levelname)s =>%(name)s =>%(message)s")
        fi_handler.setFormatter(formater)

        testCase_name = inspect.stack()[1][3]
        loggerr = logging.getLogger(testCase_name)
        loggerr.addHandler(fi_handler)
        loggerr.setLevel(logging.INFO)

        return loggerr
