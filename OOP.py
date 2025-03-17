'''
Requirements for OOP implementation
    1. abstract class File
        o Attributes: name, size, content.
        o Open(self) method that opens the file and performs an action (type-dependent).
        o The delete(self) method, which ‘deletes’ the file.
    2. Different file types (File inheritors)
        o Text file (TextFile) - can read text (read()), append()).
        o Media file (MediaFile) - can play (play()).
        o Executable file (ExecutableFile) - can run (run()).
    3. Work with files
        o Create a list of different types of files.
        o Write code that randomly ‘works’ with different files.

Example of how the system works
text = TextFile(‘story.txt’, ‘Once upon a time there was a cat...’)
video = MediaFile(‘movie.mp4’, size=700)
exe = ExecutableFile(‘setup.exe’, size=150)
text.open() # ‘Open story.txt: Once upon a time there was a cat...’
video.play() # ‘Movie.mp4 is playing’
exe.run() # ‘Started setup.exe’

Restrictions:
- It is forbidden to use if in open().
- Files must ‘take up space’.
- Methods in all classes must be unique. 
'''

# Started from imported libraries Abstract Base Classes, OS
from abc import *
import os

class File(ABC):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    
    @abstractmethod
    def open(self):
        pass

    def delete(self):
        if os.path.exists(self.name): # Check existing of the file
            os.remove(self.name)
            print("File has been deleted")
        else:
            print("File doesn't exist")

    def info(self):
        if os.path.exists(self.name): # Size in real bytes 
            file_stats = os.stat(self.name)
            print(f"File: {self.name}. Size: {file_stats.st_size} bytes")
        else:
            print("File does not exist")

# Text files 
class TextFile(File):
    def __init__(self, name):

        if os.path.exists(name):
            with open(name, 'r') as file:
                content = file.read()
            size = os.path.getsize(name)
        else:
            content = ""
            size = 0

        super().__init__(name, size ,content) # Inheritance from parent (file)

    def open(self):
        self.read()

    def read(self):
        if self.content:
            print(self.content)
        else:
            print("File is empty")

    def append(self, text):
        with open(self.name, 'a') as file: # 'a' - append. Opens a file for appending, creates the file if it does not exist
            file.write(text)
        self.content += text

# Video files
class MediaFile(File):
    def __init__(self, name):
        if os.path.exists(name):
            size = os.path.getsize(name)
            content = "Media content"
        else:
            content = ""
            size = 0
        super().__init__(name, size ,content)

    def open(self):
        self.play()

    def play(self):
        if os.path.exists(self.name):
            os.startfile(self.name) # Using base Windows media player
        else:
            print("File does not exist")

# Executable files
class ExeFile(File):
    def __init__(self, name):
        if os.path.exists(name):
            size = os.path.getsize(name)
            content = "Executable content" 
        else:
            content = ""
            size = 0
        super().__init__(name, size ,content)
    
    def open(self):
        self.run()
    
    def run(self):
        if os.path.exists(self.name):
            os.startfile(self.name)
        else:
            print("File does not exist")

# Interaction
while True:
    try:
        x = int(input("Choose 1: TXT File. Option 2: MP4 File. Option 3: EXE File Option 4: Exit \n"))
        
        if x == 4:
            break
        if x not in [1, 2, 3]:
            print("Not an option")
            continue
        else:
            FileName = input("Write file name with extension (.txt, .mp4, .exe). You can also specify a path to the file but do not forget about extension. \n")

        z = input("What you want? \n 1. File Info \n 2. File Read/Play/Execute \n 3. File Permanent Delete \n 4. Back \n")

        if z == 4:
            print("Back to choose")
            break
        if z not in ["1", "2", "3", "4"]:
            print("Not an option")
            continue

        match x:
            
            case 1:
                text_file = TextFile(FileName)
                if z == "1":
                    text_file.info()
                if z == "2":
                    y = input("Do you want to edit your file? yes/no \n")
                    if y == "yes" or y == "Yes":
                        fileAppend = input("Enter text to append: ")
                        text_file.append(fileAppend)
                    text_file.open()
                if z == "3":
                    text_file.delete()

            case 2:
                media_file = MediaFile(FileName)
                if z == "1":
                    media_file.info()
                if z == "2":
                    media_file.open()
                if z == "3":
                    media_file.delete()

            case 3:
                exe_file = ExeFile(FileName)
                if z == "1":
                    exe_file.info()
                if z == "2":
                    exe_file.open()
                if z == "3":
                    exe_file.delete()

    except FileNotFoundError:
        print("File not found.")
