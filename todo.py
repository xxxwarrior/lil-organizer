import datetime 

date = datetime.date.today().strftime("%d.%m.%y")

class ToDo:
    def __init__(self):
        self.name = f"To-do for {date}"

    def create(self):   

        todoFile = open(f'{self.name}.txt', "w+")
        content = []

        index = 1
        while True:
            line = input(f"{index}. ")
            if line: 
                content.append(f"{index}. " + line)
                index += 1
            else: break     
        todoFile.write("\n".join(content))
        todoFile.close()
