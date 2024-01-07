print(list('Hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)
for letter in name:
    print(letter) 
    
# list and strings are different because lists are mutable (liable to change) 
# whereas strings are immutable (not liable to change)

name = 'Zophie the cat'
print(name[7])
# name[7] = 'x' - will not change the value

# proper way to modify a string is with slices
name2 = 'Zophie a cat'
newName = name2[0:7] + 'the' + name2[8:]
print(newName)  