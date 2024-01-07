spam = 0
while spam < 5:
    spam = spam + 1
    if spam % 2 == 0:
        continue
    print('spam is ' + str(spam))