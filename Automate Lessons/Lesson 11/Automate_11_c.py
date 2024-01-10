import shutil # shell utilities
shutil.copy('C:\\Users\\David Huang\\Downloads\\Python\\bacon.txt', r'C:\Users\David Huang\Downloads')
# shutil.copy() copies a file from one location to another
shutil.copy('C:\\Users\\David Huang\\Downloads\\Python\\bacon.txt', r'C:\Users\David Huang\Downloads\spamspamspam.txt')
# you can also copy and rename at the same time by designating the destination file name
try:
    shutil.copytree(r'C:\Users\David Huang\Downloads\Python',r'C:\Users\David Huang\Downloads\PythonBackup')
except Exception:
    print("Error copying files")
# shutil.copytree() copies a directory from one location to another
try:
    shutil.move(r'C:\Users\David Huang\Downloads\spamspamspam.txt',r'C:\Users\David Huang\Downloads\PythonBackup')
except Exception:
    print("Error moving files")
# to rename a file, use shutil.move() on a file and designate a new file name
shutil.move(r'C:\Users\David Huang\Downloads\spamspamspam.txt',r'C:\Users\David Huang\Downloads\spammyspam.txt')
