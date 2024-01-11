'''
************
*          *
*          *
*          *
************

'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be a single character')
    if (width < 2) or (height < 2):
        raise Exception('width and height must be greater than 2')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)    
 
boxPrint('*', 10, 5)
    
boxPrint('O', 5, 7)

boxPrint('*', 10, 5)

import traceback
try: 
    raise Exception('This is an error message')
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc() + '\n')
    errorFile.close()
    print('The traceback info was written to the error_log.txt')
    
import os
print(os.getcwd())

assert False, 'This is an error message'
    