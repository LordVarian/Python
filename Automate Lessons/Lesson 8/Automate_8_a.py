# escape characters

print("That is Alice's cat.")
print("Say hi to Bob\'s mother.")

# \' is a single quote
# \" is a double quote
# \t is a tab
# \n is a new line
# \\ is a backslash

print("Hello there!\nHow are you?\nI\'m fine.")
print(r"That is Carol\'s cat.")
# adding r to a string will make it a raw string that will include the backslashes

print("""Dear Alice, 
      Eve's cat has been arrested for catnapping, 
      cat burglary, and extortion. 
Sincerely Bob.""")
# multi-line strings are very useful when you have a lot of text

spam = "Hello World!"
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('Hello' in spam)
print('X' in spam)
print('HELLO' in spam) 
print('HELLO' in spam.upper())  
# case sensitive