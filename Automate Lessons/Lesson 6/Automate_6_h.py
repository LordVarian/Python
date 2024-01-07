def eggs(someParamter):
    someParamter.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)
# print function call in the global scope is still seeing the change from the function call 
# in the local scope. This can lead to many problems and bugs.

import copy
fam = ['A', 'B', 'C', 'D']
ham = copy.deepcopy(fam)
ham[1] = 42
print(ham)
print(fam)
# by making a copy of a list, we can make a changes to the copy of the list without
# affecting the original

spam = ['apples',
        'oranges',
        'pears',
        'bananas']

print('Four score and seven ' + \
        'years ago')
# line continuation
