import datetime
import os
from pynput.keyboard import Key, Controller, Listener 

class Notebook:
    def __init__(self, notebookNum):
        self.notebookNum = 1
        self.notes = []
        self.note_id = 0
        self.cwd = os.getcwd()                        #Dont forget to add delete option for both notes and notebooks

    def createNotebook(self):
        os.mkdir(f'{self.cwd}\Notebook{self.notebookNum}')
        print(f"Your notebook is created in {self.cwd}")


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






    