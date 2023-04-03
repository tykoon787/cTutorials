def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol Must be a single character String")
    if width < 2:
        raise Exception("Width Must be greater than 2")
    if height <= 2:
        raise Exception("Height Must be greater than 2")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * 2)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print(f'An Exception Happened {str(err)}')

print('-------------------------------')
print('Reading Traceback Calls')
print('-------------------------------')


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()

# From the traceback, you can see that the error happened on line 5, in
# the bacon() function. This particular call to bacon() came from line 2, in the
# spam() function, which in turn was called on line 7.

print('---------------------------------------------------------------')
print('Getting TraceBacks as a string using the traceback.format_exc()')
print('This will help you log errors in a file and let the program run')
print('---------------------------------------------------------------')

import traceback

try:
    raise Exception("This is the error Message")
except:
    errorFile = open('ErrorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Errors written to ErrorInfor.txt')

    print('-------------------------------')
    print('Assertions')
    print('-------------------------------')

    # Assertions are for programmer errors not user errors

    ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
    ages.sort()
    print(ages)

    assert ages[0] <= ages[
        -1]  # The assert statement here asserts that the first item in ages should be less than or equal to the last one

    # Because the expression is true, the assert statement does nothing

    ages.reverse()
    print(ages)

    assert ages[0] <= ages[-1]  # Becasue the assertion here is false, we get an assertion Error

    print('-------------------------------')
    print('Logging with the Logging Module')
    print('-------------------------------')

    import logging

    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname) s - %(message)s')


    def factorial(n):
        logging.debug(f'Start of Factorial {n}')
        total = 1
        for i in range(1, n + 1):
            total *= i
            logging.debug(f'i is {str(i)}, total is {str(total)}')
        logging.debug(f'End of Factorial {n}')
        return total


    print(factorial(5))
    logging.debug('End of Program')

print('-------------------------------')
print('Disabling Logging')
print('-------------------------------')

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.critical('Critical Error')
logging.disable(logging.CRITICAL)
logging.critical('Another Critical Error')
logging.error('Just a usual Error')

print('\nNotice How loggind has been disabled?')

print('-------------------------------')
print('Logging Into a File')
print('-------------------------------')

import logging
from pathlib import Path

loggingFile = 'myProgramLog.txt'
logging.basicConfig(filename=loggingFile, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def factorial(n):
    logging.debug(f'Start of Factorial {n}')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {str(i)}, total is {str(total)}')
    logging.debug(f'End of Factorial {n}')
    return total


print(factorial(5))
logging.debug('End of Program')

cwd = Path.cwd()
print(f'Log Saved in {loggingFile} at {cwd}\\{loggingFile}')
