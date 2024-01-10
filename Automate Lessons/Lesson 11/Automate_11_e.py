import os, shutil

for folderName, subFolders, fileNames in os.walk(r'C:\Users\David Huang\Downloads\PythonBackup'):
    print('The folder is: ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(fileNames))
    print()
    
    for subfolders in subFolders:
        print(subFolders)
        # subFolders.unlink() 
        if 'fish' in subFolders:
            os.rmdir(subFolders)
            
    for file in fileNames:
        if file.endswith('.py'):
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))