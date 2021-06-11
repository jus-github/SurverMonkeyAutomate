import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(".//Logs//automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger


























# import logging
# import  sys
#
# class LogGen:
#     @staticmethod
#     def loggen():
#
#         logging.basicConfig(filename="Test.log", level=logging.INFO)
#         logger=logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
#                                       '%m-%d-%Y %H:%M:%S')
#         stdout_handler = logging.StreamHandler(sys.stdout)
#         stdout_handler.setLevel(logging.DEBUG)
#         stdout_handler.setFormatter(formatter)
#
#         file_handler = logging.FileHandler('.\\Logs\\Test.log')
#         file_handler.setLevel(logging.DEBUG)
#         file_handler.setFormatter(formatter)
#
#         logger.addHandler(file_handler)
#         logger.addHandler(stdout_handler)
#         return logger










































