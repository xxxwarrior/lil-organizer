import os
import appDirectories


class Note:
    def __init__(self, note_id, name, tags=[]):
        self.name = name
        self.id = note_id       
        self.tags = tags

    def create(self):
        note = open(f'{self.name}.txt', "w+")
        content = []

        print("""When you finish your note type 
    'End' on a new line""")   
          
        while True:
            line = input()
            if line.lower() == "end": break
            content.append(line)
        content.append(f"\nTags: {', '.join(self.tags)}")
        note.write("\n".join(content))
        note.close()







    