# Import the necessary modules
import os
import shutil

# We define a path
path = "D:/games"

# We create a list of all the files
list = os.listdir(path) 

# loop through each file
for file in list:
    # Split the name and extension
    name , ext = os.path.splitext(file)
    # removes the "."
    ext = ext[1:]
    # There is no extension
    if ext == '':
        continue
    # if there is already a folder for select extension
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    # Else create a folder and move the file there
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)


