helloFile = open(r"C:\Users\David Huang\Downloads\hello.txt")
# opens a file for reading
content = helloFile.read()
# reads the content of the file and saves to a variable (returns a single string)
print(content)
# prints the content of the file
helloFile.close()
# closes the file
helloFile = open(r"C:\Users\David Huang\Downloads\hello.txt")
print(helloFile.readlines())
helloFile.close()
# readlines prints the contents into a list
# helloFile = open(r"C:\Users\David Huang\Downloads\hello.txt", 'w') write mode will overwrite
# helloFile = open(r"C:\Users\David Huang\Downloads\hello.txt", 'a') append mode will append
# if the file doesn't exist, it will be created for both write and append modes
helloFile2 = open(r"C:\Users\David Huang\Downloads\hello.txt", 'w')
helloFile2.write("Hello World!!!!!!!!!!!")
helloFile2.write("Hello World!!!!!!!!!!!")
helloFile2.write("Hello World!!!!!!!!!!!")
helloFile2.close()

baconFile = open('bacon.txt', 'w')
baconFile.write("I love bacon! Bacon is not a vegetable. ")
baconFile.close()
import os
print(os.getcwd())
baconFile2 = open('bacon.txt', 'a')
baconFile2.write("\nbacon is delicious.")
baconFile2.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Larry', 'Billy', 'Fred']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

# shelf file objects are very similar to dictionaries
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()