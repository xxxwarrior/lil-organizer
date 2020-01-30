import datetime 

date = datetime.date.today().strftime("%d.%m.%y")

class ToDo:
    def __init__(self):
        self.name = f"To-do for {date}"

    def create(self):   

        todoFile = open(f'{self.name}.txt', "w+")
        content = []

        counter = 1
        while True:
            strNumber = f"{counter}. "
            line = input(strNumber)
            if line: counter += 1
            else: break
            content.append(strNumber+line)
        todoFile.write("\n".join(content))
        todoFile.close()
