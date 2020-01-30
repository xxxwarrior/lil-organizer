import os
import appDirectories
from notebook import Note
from datetime import datetime
from notification import Notification
from multiprocessing import Process 
from todo import ToDo



class Menu:    
    def __init__(self):
         self.menuOptions = {}
    
    def displayMenu(self):
        """ 
        Displays the name of the methods from self.menuOptions
        The functions works properly only for camelCase names

        For example showMyNotes() will be displayed as
        1. Show My Notes

        """

        print("\n")
        for num, func in enumerate(self.menuOptions.values(), 1):
            name = "".join([" "+ i if i.isupper() else i for i in func.__name__])
            print(f'{num}: {name.title()}')
        print("\n")

    def run(self):    #stop=False
        while True: 
            self.displayMenu()
            choice = input("Enter a menu number: ")
            action = self.menuOptions.get(choice)
            if action: action()
            else: print(f"{choice} is invalid choice")

    def quit(self):
        print("Are you sure you want to quit? [y/n]")
        choice = input()
        if 'y' in choice.lower():
            print("""Thank you for using this app
                Have a productive day""")
            quit()
        else: pass

    def mainMenu(self):    # This isn't right
        MainMenu().run()   # This isn't right AT ALL

###
class MainMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.notes,                 
            "2": self.reminder,              
            "3": self.toDo,                  
            "4": self.goals,                 
            "5": self.activities,           
            "6": self.quit,           
        }
    
    def notes(self):
        NotesMenu().run()
    def reminder(self):
        ReminderMenu().run()
    def toDo(self):
        ToDoMenu().run()
    def goals(self):
        GoalsMenu().run()
    def activities(self):
        ActivitiesMenu().run()
    




###
class NotesMenu(Menu):    
    def __init__(self):
        self.menuOptions = {
            "1": self.addNewNote,
            "2": self.findANote,
            "3": self.mainMenu,
            "4": self.quit,
        }
        os.chdir(appDirectories.notes_dir)
        self.notes = [i for i in os.scandir(appDirectories.notes_dir) if i. is_file()]
        self.note_id = 0

    def displayMenu(self):        
        print("\n")
        if not self.notes:
            print("You don't have any notes yet")
        else: 
            print("\nYour notes:\n")
            for num, note in enumerate(self.notes, 1):
                print(f'{num}. {note.name}')
        print("\n")
        super().displayMenu()

                 

    def addNewNote(self):
        self.note_id += 1
        name = input("Name your note or press Enter\n")
        if not name: name = f"Note{self.note_id}"
        else:
            import re # To avoid invalid input 
            reg = re.compile("[^a-zA-Z][^0-9]")
            name = reg.sub('', name)
        tags = input("Add some tags or press enter\n")
        note = Note(self.note_id, name, tags.split())
        try:
            note.create()
        except FileExistsError:
            print(f"Note '{name}' already exists")  



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
    
    def setSingleReminder(self):
        message = input("Enter the reminder message: ")        
        date = datetime.today().strftime("%Y.%m.%d,")
        done = False
        while not done:
            try:
                time = input("\nSet the time, for example '12:30'\n") 
                dateObj = datetime.strptime(date+time, '%Y.%m.%d,%H:%M')
                n = Notification(message=message, when=dateObj)
                process = Process(target=n.activate)
                process.start()
                done = True
            except ValueError:
                print("The time format is invalid, try again")
        print("Your reminder was set successfully")

    def setRepeatedReminder(self):
        print("Let's encourage your memory couse there's no such functionality here")
        print("hehe")


###
class ToDoMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyToDo,
            "2": self.createToDoList,
            "3": self.mainMenu,
        }
        
        os.chdir(appDirectories.todos_dir)


    def showMyToDo(self):
        date = datetime.today().strftime("%d.%m.%y")
        todos = [i for i in os.listdir(appDirectories.todos_dir)]
        if todos != []:
            for i in todos:
                if date in i:
                    f = open(i, "r")
                    print("\n", f.read(), sep="")
                    f.close()
        else: print("There are no to-dos for today")
             

    def createToDoList(self):
        inp = input("""If you already have to-do list for today, 
        this action will rewrite it. Continue? [y/n]\n""")
        if "y" in inp:
            ToDo().create()

    def displayMenu(self):
        print('''
1. Show my to-do for today
2. Create new to-do list
3. Main Menu
        ''')


###
class GoalsMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyGoals,
            "2": self.addNewGoal,
            "3": self.addAListOfGoals,
            "4": self.mainMenu,
        }

    def showMyGoals(self):
        pass
    def addNewGoal(self):
        pass
    def addAListOfGoals(self):
        pass


###
class ActivitiesMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.addNewActivity,

            "4": self.mainMenu,

        }
    def displayMenu(self):
        print("""\nIn this section you can keep track of your activities\n
            such as reading or meditation on everyday basis""")
        super().displayMenu()

    




if __name__ == "__main__":
    appDirectories.run()
    MainMenu().run()
    




