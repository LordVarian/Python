spam = ["cat","bat","rat","dog","mouse","rabbit"]
print(spam[2])
print(spam[-1])

bam = [["cat","bat","rat","dog","mouse","rabbit"], [10, 20, 30, 40, 50, 60]]
print(bam[1])

print("The " + spam[3] + " is afraid of the " + spam[-2])

print(spam[1:4])

lam = [1,2,3,4,5,6,7,8,9,10]
lam[5] = "Hello"
lam[0:3] = ["Hello", "World", "dog"]
print(lam)

cam = ["cat","bat","rat","dog","mouse","rabbit"]
print(cam[:2])
print(cam[1:])

mam = ["cat","bat","rat","dog","mouse","rabbit"]
del mam[3]
print(mam)

print(len([1,2,3,4,5,6,7,8,9,10]))
print([1,2,3] + [4,5,6])
print("Hello" * 3)

print(list('Hello'))

print("Howdy" in ['Hello', 'World', 'dog', 'Howdy'])
print("Howdy" not in ['Hello', 'World', 'dog', 'Howdy'])