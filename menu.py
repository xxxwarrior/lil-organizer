import os
import appDirectories
import notebook
from notebook import Notebook, Note



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

        for num, func in enumerate(self.menuOptions.values(), 1):
            name = "".join([" "+i if i.isupper() else i for i in func.__name__])
            print(f'{num}: {name.title()}')

    def run(self):
        while True: 
            self.displayMenu()
            choice = input("Enter a menu number: ")
            action = self.menuOptions.get(choice)
            if action: action()
            else: print(f"{choice} is invalid choice")

    def mainMenu(self):
        MainMenu().run()

###
class MainMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.notes,                # 1. Notes 
            "2": self.reminder,             # 2. Reminder 
            "3": self.toDo,                 # 3. To-Do 
            "4": self.goals,                # 4. Goals 
            "5": self.activities, 
            "6": self.quit,          # 5. Activities 
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
    
    def quit(self):
        print("Are you sure you want to quit? [y/n]")
        choice = input()
        if choice.lower() == 'y':
            print("""Thank you for using this app
                Have a productive day""")
            quit()
        else: pass




###
class NotesMenu(Menu):    
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyNotebooks,
            "2": self.createNewNotebook,
            "3": self.addNewNote,
            "4": self.findANote,
            "5": self.mainMenu,
        }
    
    def showMyNotebooks(self):
        os.chdir(appDirectories.notebooks_dir)

        # The list of folders in Notebooks folder:
        notebooks = [i.name for i in os.scandir(os.getcwd()) if i.is_dir()]

        if not notebooks:
            print("You don't have any notebooks yet")
        else:
            print("\nYour notebooks:\n")
            for num, name in enumerate(notebooks, 1):
                print(f'{num}. {name}' )
        print("\n")


    def createNewNotebook(self):
        Notebook()       
        Notebook.notebook_id += 1 

    def addNewNote(self):
        pass
        # Notebook.addNote()
    def findANote(self):
        pass


###
class ReminderMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.setSingleReminder,
            "2": self.setRepeatedReminder,
            "3": self.setQuestionForYourself,
            "4": self.mainMenu,
        }
    
    def setSingleReminder(self):
        pass
    def setRepeatedReminder(self):
        pass
    def setQuestionForYourself(self):
        pass


###
class ToDoMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyToDo,
            "2": self.createToDoList,
            "3": self.mainMenu,
        }

    def showMyToDo(self):
        pass
    def createToDoList(self):
        pass

    def displayMenu(self):
        print('''
        1: Show my to-do's
        2: Create a to-do list
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
            "4": self.mainMenu,

        }


if __name__ == "__main__":
    appDirectories.run()
    MainMenu().run()
    




