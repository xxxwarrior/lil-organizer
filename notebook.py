import datetime
import os
import appDirectories
from pynput.keyboard import Key, Controller, Listener 

cwd = os.getcwd()
        
#Dont forget to add delete option for both notes and notebooks

class Notebook:
    """The instance of the class creates the folder in cwd to store user's notes"""

    notebook_id = 1
    directory = appDirectories.notebooks_dir
    
    def __init__(self):
        # Create new folder in the Notebooks directory
        os.mkdir(f'{Notebook.directory}\\Notebook{Notebook.notebook_id}')

        self.notes = []
        self.note_id = 0


    def addNote(self, noteName=""):
        self.note_id += 1
        noteName = input("Name your note or press Enter\n")
        if not noteName:
            noteName = f"Note{self.note_id}"
        Note(self.note_id, noteName).create()


class Note:
    def __init__(self, note_id, noteName):
        self.creationDate = datetime.date.today
        self.noteName = noteName

    def create(self):
        note = open(self.noteName, "w+")
        hotkey = False
        content = []

        def hotkeyPressed(key):
            if key == Key.shift and Key.enter:
                hotkey = True
        with Listener(on_press=hotkeyPressed) as listener:
            listener.join

        print("""When you finish your note press Shift+Enter\n
                or type 'End Note' on a new line""")
        while True:
            line = input()
            if line:
                content.append(line)
            elif hotkey or line.lower() == "end note":
                break
        note.write("\n".join(content))
        note.close()


def createNotebooksFolder():
    try:
        os.mkdir(f"{cwd}\\Notebooks")
    except FileExistsError:
        pass







    