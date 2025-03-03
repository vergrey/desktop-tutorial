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

class file(ABC):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    @abstractmethod
    def open(self):
        pass # That's for everyone unique
    
    def delete(self):
        if os.path.exists(self.name): # Check existing of the file
            os.remove(self.name)
        else:
            print("File doesn't exist")

    def info(self):
        try:
            self.size = os.stat(self.name).st_size # Size in real bytes 
        except FileNotFoundError:
            return 0
        print("Size: {self.size}")

# Text files  
class text(file):
    def __init__(self, name, size, content):
        super().__init__(name, size ,content) # Inheritance from parent (file)
    
    def open(self):
        print({self.content}) 

    def read(self):
        return self.content

    def append(self, text):
        self.content += text

# Video files
class media(file):
    def __init__(self, name, size, content):
        super().__init__(name, size ,content)

    def play(self):
        os.startfile(self.name) # Using base Windows media player

# Executable files
class exe(file):
    def __init__(self, name, size, content):
        super().__init__(name, size ,content)
    
    def run(self):
        os.startfile(self.name)