spam = ['cat', 'dog', 'bat']
spam.append('mouse')
print(spam)
spam.insert(2, 'rabbit')
print(spam)

cam = ['cat','bat','rat','dog','mouse','rabbit']
cam.remove('bat') 
# allows for specific values to be removed rather than the index positon compared to below
print(cam)

del cam[1]
print(cam)

fam = [2, 5, 3.14, 1, -5]
fam.sort()
print(fam)
fam.sort(reverse=True)
print(fam)

# can't sort a list of values with both strings and numbers

sam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
sam.sort()
# capitals are sorted alphabetically first before lower case
print(sam)

nam = ['a', 'z', 'A', 'Z']
nam.sort(key=str.lower)
# sorts in true alphabetic order
print(nam)