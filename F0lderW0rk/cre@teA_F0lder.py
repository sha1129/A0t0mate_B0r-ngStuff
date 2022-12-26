# Create folder
import os

# Set the base path and the number of folders to create
# r to read raw and folder path = where you want to create
base_path = r'folder path' 

# number of folder that needed to be created
num_folders = 3

# Use a for loop to create the folders
for i in range(num_folders):
    # Set the folder name and path
    folder_name = 'Lecture ' + str(i+1)
    folder_path = os.path.join(base_path, folder_name)
    
    # Create the folder
    # mkdir() function is used to create the folders
    os.mkdir(folder_path)

print('Folders created!')
