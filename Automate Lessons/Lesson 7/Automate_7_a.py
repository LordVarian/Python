# Dictionary data type

myCat = {'size': 'fat', 'color': 'brown', 'disposition': 'happy'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur')

spam = {12345: 'Luggage combination', 42: 'The Answer'}
print([1,2,3] == [3,2,1])
# order matters for lists

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
# however, order does not matter for dictionaries

print(eggs == ham)

print('name' in eggs)
print('name' not in ham)
# keep in mind that like lists, dictionaries are mutable

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)
    
for v in eggs.values():
    print(v)
    
for k, v in eggs.items():
    print(k + ': ' + str(v))
    
for i in eggs.items():
    print(i)
# prints out tuples - which are the same as lists but are immutable and use parentheses instead
# of square brackets

print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])
    
eggs.get('age', 0)
eggs.get('color', '')

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic')
# without the get() method, the value of the key will be returned if the key does not exist
# this will result in a KeyError

if 'color' not in eggs:
    eggs['color'] = 'brown'
    
eggs.setdefault('color', 'brown')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)
# the second setdefault will not change anything since the color key already exists