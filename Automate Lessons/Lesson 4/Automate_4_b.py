print("How many cats do you have?")
numCats = input()

try:
    if int(numCats) >= 4:
        print("That is a lot of cats!")
    elif int(numCats) < 0:
        print("You can't have a negative number of cats.")
    else:
        print("That is not that many cats.")
except ValueError:
    print("That is not a number.")