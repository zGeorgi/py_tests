import inspect
import logging

def test_loggingsDemo():
# this method create object
#catch the file_name and print it on the log
    log_name = inspect.stack()[1][3] #test case name
    logger = logging.getLogger(log_name)  # or current filename __name__

# describe the name of the loggind_file and location to be created
    file_handler = logging.FileHandler('logfile.log')

#create forrmat on the stored messages
#logging.Formatter("%(time)s :%(type_of_log_msg)s :(file_name)s :%(message)s")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s FileName: <%(name)s> Message: <%(message)s>")

# get formatter settings in the FileHandler object
    file_handler.setFormatter(formatter)

#take the "FileHandler" object like parameter to manipulate it
    logger.addHandler(file_handler)

# set from what level to be print the messages
    logger.setLevel(logging.INFO)
# this is hierarchy of logs printing
# if the warning is set only steps after it will be printed (error and critical)
#and first two (debug and info) will be skiped
    logger.debug("A debug statment is execute")
    logger.info("Information statment")
    logger.warning("warning msg")
    logger.error("A major error has ocure")
    logger.critical("Critical issue")