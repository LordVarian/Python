#This is a guess the number game.
import random
print("Hello. What is your name?")
name = input()

num1 = 1
num2 = 20

secretNumber = random.randint(num1, num2)
print ("Well, " + name + " I am thinking of a number between " + str(num1)+ " and " + str(num2) + ".")

for guessesTaken in range(1,7):
    print ("Take a guess")
    try:
        guess = int(input())
    except ValueError:
        print("That is not a number.")
        continue

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
try:
    if guess == secretNumber:
        print("Good job, " + name + "! You guessed it in " + str(guessesTaken) + " guesses.")
    else:
        print("Nope. The number I was thinking of was " + str(secretNumber) + ".")
except NameError:
    print("guess was not defined, cause your dumbass didn't enter an actual number.")