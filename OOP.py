'''
Требования к ООП-реализации
    1. Абстрактный класс File (Файл)
        o Атрибуты: name (название), size (размер), content (содержимое).
        o Метод open(self), который открывает файл и выполняет действие (зависит от типа).
        o Метод delete(self), который "удаляет" файл.
    2. Разные типы файлов (наследники File)
        o Текстовый файл (TextFile) – умеет считывать текст (read()), дописывать (append()).
        o Медиафайл (MediaFile) – умеет проигрываться (play()).
        o Исполняемый файл (ExecutableFile) – умеет запускаться (run()).
    3. Работа с файлами
        o Создай список файлов разных типов.
        o Напиши код, который случайным образом "работает" с разными файлами.

Пример работы системы
text = TextFile("story.txt", "Жил-был кот...")
video = MediaFile("movie.mp4", size=700)
exe = ExecutableFile("setup.exe", size=150)
text.open() # "Открыт story.txt: Жил-был кот..."
video.play() # "Проигрывается movie.mp4"
exe.run() # "Запущен setup.exe"

Ограничения:
• Запрещено использовать if в open() (используй полиморфизм).
• Файлы должны "занимать место" (размер не просто так).
• Методы у всех классов должны быть уникальными. 
'''

# Started from imported libraries Abstract Base Classes, OS, System, Platform
from abc import *
import os
import sys
import platform

class File(ABC):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    
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

    def read(self):
        print(self.content)

    def append(self, text):
        with open(self.name, 'a') as file:
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

    def play(self):
        os.startfile(self.name) # Using base Windows media player

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
    
    def run(self):
        os.startfile(self.name)


# Interaction
x = int(input("Option 1: Open TXT. Option 2: Open MP4. Option 3: Open EXE \n"))

if x not in [1, 2, 3]:
    print("Not an option")
else:
    FileName = input("Write file name with extension (.txt, .mp4, .exe) \n")

match x:
    case 1:
        text_file = TextFile(FileName)
        y = input("Do you want to edit your file? yes/no \n")
        if y == "yes" or y == "Yes":
            fileAppend = input("")
            text_file.append(fileAppend)
        else:
            pass
        text_file.info()
        text_file.read()
    case 2:
        media_file = MediaFile(FileName)
        media_file.info()
        media_file.play()
    case 3:
        media_file = ExeFile(FileName)
        media_file.info()
        media_file.run()
    case _:
        print("Doesn't exist")