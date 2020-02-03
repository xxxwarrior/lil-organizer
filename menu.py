import os
import re 
import colorama
from datetime import datetime

import appDirectories
from todo import ToDo
from note import Note
from notification import Notification

colorama.init()
color = "\033[36;49;1m" # bright cyan 

class Menu:    
    def __init__(self):
         self.menuOptions = {}
         self.color = color
    
    def displayMenu(self):
        """ 
        Displays the name of the methods from self.menuOptions
        The functions works properly only for camelCase names

        For example showMyNotes() will be displayed as
        1. Show My Notes

        """
        print("\n")
        print(self.color)
        for num, func in enumerate(self.menuOptions.values(), 1):
            name = "".join([" "+ i if i.isupper() else i for i in func.__name__])
            print(f'{num}: {name.title()}')
        print("\n")

    def run(self):
        while True: 
            self.displayMenu()
            choice = input("Enter a menu number: ")
            action = self.menuOptions.get(choice)
            if action: action()
            else: print(f"'{choice}' is invalid choice")


    def quit(self):
        # Maybe one day you'll figure out the way to do it more elegant 

        string = ' ' * 37 
        print("\033[41;1m", string) # red bg     
        print("\033[42;1m", string) # green bg        
        print("\033[43;1m", string, end='') # yellow bg 
        print("\033[37;45;1m") # white text & magenta bg 

        choice = input("Are you sure you want to quit? [y/n] ")
        print("\033[45;1m", string)
        if 'y' in choice.lower():  
            print("""Thank you for using this app          
        Have a productive day!        """)
            print("\033[41;1m", string)
            print("\033[42;1m", string)
            print("\033[43;1m", string)
            quit()
        print(color)

    def mainMenu(self):    # This isn't right
        MainMenu().run()   # This isn't right AT ALL

###
class MainMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.notes,                 
            "2": self.reminder,              
            "3": self.toDo,                                  
            "4": self.activities,           
            "5": self.quit,           
        }
        self.color = color
    
    def notes(self):
        NotesMenu().run()
    def reminder(self):
        ReminderMenu().run()
    def toDo(self):
        ToDoMenu().run()
    def activities(self):
        ActivitiesMenu().run()
    



###
class NotesMenu(Menu):    
    def __init__(self):
        self.menuOptions = {
            "1": self.addNewNote,
            "2": self.openNote,
            "3": self.findANote,
            "4": self.mainMenu,
            "5": self.quit,
        }
        self.color = "\033[35;40;1m" # bright magenta
        os.chdir(appDirectories.notes_dir)
        self.notes = [i for i in os.scandir(appDirectories.notes_dir) if i.is_file()]
        self.note_id = 0 


    def displayMenu(self):        
        print("\033[30;47;2m") # black text & white bg
        if not self.notes:
            print("You don't have any notes yet")
        else: 
            print("Your notes:\n")
            for num, note in enumerate(self.notes, 1):
                print(f'{num}. {note.name}')
        super().displayMenu()
                 

    def addNewNote(self):
        name = input("Name your note or press Enter\n")
        if not name: 
            for entry in self.notes:
                if "Note" in entry.name and re.search(r'\d', entry.name):
                    reg = re.compile("[^0-9]")
                    last_id = int(reg.sub('', entry.name))
                    if last_id > self.note_id:
                        self.note_id = last_id
            self.note_id += 1
            name = f"Note{self.note_id}"
        else:
            # To avoid invalid input 
            reg = re.compile("[^a-zA-Z][^0-9]")
            name = reg.sub('', name)
        tags = input("Add some tags or press enter\n")
        note = Note(self.note_id, name, tags.split())
        try:
            print("\033[37;1m") # white text
            note.create()
        except FileExistsError:
            print(f"Note '{name}' already exists")  
            
    
    def openNote(self):
        choice = input("\nEnter the note number: ")
        for num, note in enumerate(self.notes, 1):
            if choice == str(num):
                print("\033[37;1m", f"The note '{note.name}':")
                f = open(note, "r")
                print("\n", f.read(), sep="")
                f.close()
                print(self.color)
                break
            else: pass



    def findANote(self):
        keyword = input("Enter the keyword:\n")
        if not keyword:
            print("You haven't entered anything")
        else:
            match = []
            for entry in self.notes:
                with open(f'{entry.name}', "r") as note:
                    if keyword in note.read() or keyword in entry.name: 
                        match.append(entry.name)
            if match: 
                print(f"There is '{keyword}' in {', '.join(note for note in match)}")
            else: print(f"There are no notes with '{keyword}' in it")
            
        

###
class ReminderMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.setSingleReminder,
            "2": self.setRepeatedReminder,
            "3": self.mainMenu,
        }
        self.color = "\033[33;1m" # bright yellow
    
    def setSingleReminder(self):
        message = input("Enter the reminder message: ")        
        date = datetime.today().strftime("%Y.%m.%d,")
        done = False
        while not done:
            try:
                time = input("\nSet the time, for example '12:30'\n") 
                dateObj = datetime.strptime(date+time, '%Y.%m.%d,%H:%M')
                n = Notification(message=message, when=dateObj)

                from multiprocessing import Process 
                process = Process(target=n.activate)
                process.start()
                done = True
            except ValueError:
                print("The time format is invalid, try again")
        print("Your reminder was set successfully")

    def setRepeatedReminder(self):
        print('\033[31;42;2m') # red text & green bg
        print("Let's encourage your memory cause there's no such functionality here")
        print("hehe")


###
class ToDoMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyToDo,
            "2": self.createToDoList,
            "3": self.mainMenu,
        }
        self.color = "\033[32;1m" # bright green 
        os.chdir(appDirectories.todos_dir)


    def showMyToDo(self):
        date = datetime.today().strftime("%d.%m.%y")
        todos = [i for i in os.listdir(appDirectories.todos_dir)]
        if todos == []: 
            print("You don't have any to-dos")
        else:
            for i in todos:
                if date in i:
                    f = open(i, "r")
                    print("\n", f.read(), sep="")
                    f.close()
                else: print("\nThere are no to-dos for today")
             

    def createToDoList(self):
        inp = input("""If you already have to-do list for today, 
        this action will rewrite it. Continue? [y/n]\n""")
        if "y" in inp.lower():
            ToDo().create()

    def displayMenu(self):
        print(self.color, '''
1. Show my to-do for today
2. Create new to-do list
3. Main Menu
        ''')


###
class ActivitiesMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.addNewActivity,
            "2": self.mainMenu,
        }
        self.color = "\033[31;1m" # bright red

    def displayMenu(self):
        print("""\nThis part is on rethinking process ¯\_(ツ)_/¯""")
        super().displayMenu()
    def addNewActivity(self):
        pass

    




if __name__ == "__main__":
    appDirectories.run()
    MainMenu().run()