import datetime
import os
import appDirectories


class Note:
    def __init__(self, note_id, name, tags=[]):
        self.name = name
        self.id = note_id
        self.creationDate = datetime.date.today        
        self.tags = tags

    def create(self):
        note = open(f'{self.name}.txt', "w+")
        content = []

        print("""When you finish your note type 
        'End Note' on a new line""")   
          
        while True:
            line = input()
            if line.lower() == "end note": break
            content.append(line)
        note.write("\n".join(content))
        note.close()







    