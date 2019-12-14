import notebook



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

###
class MainMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.notes,                # 1. Notes 
            "2": self.reminder,             # 2. Reminder 
            "3": self.toDo,                 # 3. To-Do 
            "4": self.goals,                # 4. Goals 
            "5": self.activities,           # 5. Activities 
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


class NotesMenu(Menu):    
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyNotebooks,
            "2": self.createNewNotebook,
            "3": self.addNewNote,
            "4": self.findANote,
        }
    
    def showMyNotebooks(self):
        pass
    def createNewNotebook(self):
        pass
    def addNewNote(self):
        notebook.Notebook.addNote()
    def findANote(self):
        pass


class ReminderMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.setSingleReminder,
            "2": self.setRepeatedReminder,
            "3": self.setQuestionForYourself
        }
    
    def setSingleReminder(self):
        pass
    def setRepeatedReminder(self):
        pass
    def setQuestionForYourself(self):
        pass


class ToDoMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyToDo,
            "2": self.createToDoList
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

class GoalsMenu(Menu):
    def __init__(self):
        self.menuOptions = {
            "1": self.showMyGoals,
            "2": self.addNewGoal,
            "3": self.addAListOfGoals
        }

    def showMyGoals(self):
        pass
    def addNewGoal(self):
        pass
    def addAListOfGoals(self):
        pass


class ActivitiesMenu(Menu):
    def __init__(self):
        self.menuOptions = {

        }


if __name__ == "__main__":
    MainMenu().run()
    




