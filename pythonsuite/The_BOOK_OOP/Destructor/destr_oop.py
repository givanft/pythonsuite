import time

class Student:

    # конструктор
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name

    def show(self):
        print('Hello, my name is', self.name)

    # деструктор
    def __del__(self):
        print('Object destroyed')

# создание объекта
s1 = Student('Emma')
# создание новой ссылки
# обе ссылки указывают на один объект
#s2 = Student('Puma')
s1.show()

# удаление ссылки s1
del s1

# добавление задержки и наблюдение за результатом
#time.sleep(5)
#print('After sleep')
s2.show()