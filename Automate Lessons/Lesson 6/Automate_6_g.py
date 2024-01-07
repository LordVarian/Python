spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

fam = [0, 1, 2, 3, 4, 5]
cheese = fam
cheese[1] = 'Hello'
print(cheese)
print(fam) 
# both are modified because they reference the same list in memory 
# immutable values don't have this problem because they can't be 
# modified "in place". They can only be replaced by new values.