class Person:
    __name = "Ivan"

    def set(self, name):
        self.__name = name

class Student(Person):
    grade = 1

prsn = Person()
print(prsn.__name)

prsn.set("Katya")
print(prsn.__name)

igor = Student()
igor.set("Igor")
print(igor.name, igor.grade)