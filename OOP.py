'''
Описание
Создать объектно-ориентированную систему управления файлами. Каждый файл ведет себя посвоему в зависимости от типа.

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

# Начнем с импорта библиотеки Abstract Base Classes 
from abc import *
import os
import sys

class file(ABC):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    
    def open(self):
        pass # Везде будет свое
    
    def delete(self):
        os.remove({self.name})
        print("Deleted")

    def info(self):
        os.stat({self}).st_size 

# Текстовые файлы  
class text(file):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    
    def open(self):
        print({self.content}) 

    def read(self):
        return self.content

    def append(self, text):
        self.content += text

# Видео файлы
class media(file):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content

    def play(self):
        self.play()

# exe файлы
class exe(file):
    def __init__(self, name, size, content):
        self.name = name
        self.size = size
        self.content = content
    
    def open(self):
        self.run() 