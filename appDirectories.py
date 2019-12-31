
import os


# The script creates 'Root Folder' called ProductivityPal
# which contains other folders for different app files,
# i.e. there's going to be Notebooks folder in the Root Folder
# where the user's notebooks are stored"""

# The directory which this file is in 
dir_path = os.path.dirname(os.path.realpath(__file__))
root = f"{dir_path}\\RootFolder"

# The paths of all the app folders
notes_dir = f"{root}\\Notes"
reminders_dir = f"{root}\\Reminders"
todos_dir =  f"{root}\\ToDos"
goals_dir = f"{root}\\Goals"
activities_dir = f"{root}\\Activities"




def run():
    # Create the Root Folder if it doesn't exist yet
    try: 
        os.mkdir(f"{dir_path}\\RootFolder")    
    except FileExistsError:
        pass
    
    try:
        os.mkdir(f"{root}\\Notes")
        os.mkdir(f"{root}\\Reminders")
        os.mkdir(f"{root}\\ToDos")
        os.mkdir(f"{root}\\Goals")
        os.mkdir(f"{root}\\Activities")
    except FileExistsError:
        pass
            


