'c:\\spam\\eggs.png'
r'c:\spam\eggs.png'
# use double backslashes or raw text to escape the backslashes in the regex

import os
pathtest = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# dynamic function that joins strings together to produce a file path relative to the OS 
print(pathtest)
print(os.sep)
# displays the OS path separator for files
print(os.getcwd())
# gets the current working directory
print(os.chdir('c:\\')) 
print(os.getcwd())
# absolute file paths always begin with the root folder, whereas relative file paths do not
# . stands for the current directory and .. stands for the parent directory
os.chdir('C:\\Users\\David Huang\\Downloads\\Python')

print(os.path.abspath('spam.png'))
print(os.path.abspath('..\\..\\spam.png'))
# converts a relative path to an absolute path
print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs('c:\\folder\\spam.png'))
# checks if a path is absolute
print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))
# relpath will return the relative path from the starting path to the other path 
print(os.path.dirname('c:\\folder1\\folder2\\spam.png'))
# dirname will return the directory name of the path
print(os.path.basename('c:\\folder1\\folder2\\spam.png'))
# basename will return the base file name of the path
print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.exists('c:\\windows\\system32\\notepad.exe'))
# checks if the file and path exists or not 
print(os.path.isfile('c:\\windows\\system32\\notepad.exe'))
# checks if the file stated is a file or not
print(os.path.isfile('c:\\windows\\system32'))
print(os.path.isdir('c:\\windows\\system32\\notepad.exe'))
# checks if the file is a directory or not
print(os.path.isdir('c:\\windows\\system32'))
print(os.path.getsize('c:\\windows\\system32'))
# getsize returns the size of the file in bytes as an integer
print(os.listdir(r'\\192.168.0.187\data\media\tv\anime'))

totalSize = 0
for filename in os.listdir('c:\\windows\\system32'):
    if not os.path.isfile(os.path.join('c:\\windows\\system32', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\windows\\system32', filename))

print(totalSize)

os.makedirs('c:\\delicious\\walnut\\waffles')
# makedirs created the directory if it does not already exist