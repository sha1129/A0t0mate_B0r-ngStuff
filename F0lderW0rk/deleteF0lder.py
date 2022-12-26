import os
import shutil

# Set the base path and the flag variable
base_path = r'folder name'
folders_remaining = True

# Set the initial value of the counter variable
i = 0

# Use a while loop to delete the folders
while folders_remaining:
    # Set the folder name and path
    # however way the folder name is there
    folder_name = str(i) + ' blah'
    folder_path = os.path.join(base_path, folder_name)
    
    # Try to delete the folder and its contents recursively
    try:
        shutil.rmtree(folder_path)
    except FileNotFoundError:
        # If the folder doesn't exist, set the flag variable to False
        folders_remaining = False
    
    # Increment the counter variable
    i += 1

print('Folders deleted!')
