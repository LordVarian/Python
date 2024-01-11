import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# to write logging to a file use:
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# this is the function to enable logging in Python
logging.disable(logging.CRITICAL)
# different levels of logging are used for different levels of importanct
# logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL (least to most important)
# disabling logging.CRITICAL will disable all logging as it is the highest level of logging
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.critical('i is %s, total is %s' % (i, total))
    return total

print(factorial(5))

logging.debug('End of program')
    