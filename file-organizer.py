# Use 'os' module to interact with the operating system
import os

# Use 'shutil' module to move/copy files
import shutil

# Get the folder path from the user
path = input("Enter Path: ")

# Get all files and folders inside the given path
files = os.listdir(path)

# Process each item in the directory
for file in files:

    # Split filename and extension
    filename, extension = os.path.splitext(file)

    if extension:
        # Remove the dot from the extension (e.g. '.jpg' -> 'jpg')
        extension = extension[1:]
    else:
        continue
    
    # Check if a folder for this extension already exists
    if os.path.exists(path+'/'+extension):

        # Move the file into the existing extension folder
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    
    else:
        # Create a new folder named after the extension
        os.makedirs(path+'/'+extension)

        # Move the file into the newly created folder
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

print("\nFiles organized successfully!")