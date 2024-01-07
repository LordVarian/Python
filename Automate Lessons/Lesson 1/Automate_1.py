# This program says hello and asks the user for their name.

print("Hello, what is your name?") # ask for the user's name
name = input()
print("Hello, " + name + "!")
print("The length of your name is: ")
print(len(name))

print("What is your age?") # ask for the user's age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")