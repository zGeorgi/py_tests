# logger
# filehandler,
# formater setformat ,
# getLogger <
# set testcase name
# retur loger
# setlevel
import inspect
import logging


class open_logger():

    def thi_logger(self):
        file_Handller = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s=> %(levelname)s => %(name)s => %(message)s")
        file_Handller.setFormatter(formatter)

        test_name = inspect.stack()[1][3]

        loger = logging.getLogger(test_name)
        loger.addHandler(file_Handller)
        loger.setLevel(logging.DEBUG)
        return loger
