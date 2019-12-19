#demo of logging module

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(message)s-%(levelname)s')
logging.debug('Start of program')

def factorial(num):
    total=1
    logging.debug('This is function')
    for i in range(1, num+1):
        total *= num
        logging.debug('i is %s', i ,'total is:%s', total)
    return total

print(factorial(5))

logging.debug('End of program')