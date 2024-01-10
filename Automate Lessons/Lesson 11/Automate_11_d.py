import os
# os.unlink('bacon.txt') will delete a single file
# os.rmdir('C:\Users\David Huang\Downloads') will delete a directory. 
# However, the directory must be empty
import shutil
# shutil.rmtree(r'C:\Users\David Huang\Downloads\PythonBackup') will delete a folder and all its contents

os.chdir(r'C:\Users\David Huang\Downloads')

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        
import send2trash
send2trash.send2trash(r'C:\Users\David Huang\Downloads\spammyspam.txt')
# custom module send2trash will send a file or folder to the recycling bin