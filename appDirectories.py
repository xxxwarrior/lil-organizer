import os

# The script creates 'Root Folder', which contains 
# other folders for different app files,
# i.e. there's going to be 'Notes' folder in the Root Folder
# where the user's notes are stored



# The directory which this file is in 
dir_path = os.path.dirname(os.path.realpath(__file__))
root = f"{dir_path}\\RootFolder"

# The paths of all the app folders
notes_dir = f"{root}\\Notes"
todos_dir =  f"{root}\\ToDos"
activities_dir = f"{root}\\Activities"


def run():
    # Create the Root Folder if it doesn't exist yet
    try: 
        os.mkdir(f"{dir_path}\\RootFolder")    
    except FileExistsError:
        pass
    
    try:
        os.mkdir(f"{root}\\Notes")
        os.mkdir(f"{root}\\ToDos")
        os.mkdir(f"{root}\\Activities")
    except FileExistsError:
        pass
            


