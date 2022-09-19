#''''''''''''''''''''''''''''''''''''''''''''''
class Wizard:
#''''''''''''''''''''''''''''''''''''''''''''''
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"{self.name}"

#''''''''''''''''''''''''''''''''''''''''''''''
class Student(Wizard):
#''''''''''''''''''''''''''''''''''''''''''''''
    def __init__(self, name, house, age):
        super().__init__(name)
        self.house = house
        self.age = age

    def __str__(self):
        return f"{super().__str__()} from {self.house}"

    def __add__(self, other):
        age = self.age + other.age
        return age



#''''''''''''''''''''''''''''''''''''''''''''''
class Professor(Wizard):
#''''''''''''''''''''''''''''''''''''''''''''''
    def __init__(self, name, subject, age):
        super().__init__(name)
        self.subject = subject
        self.age = age

    def __str__(self):
        return f"{super().__str__()} teach {self.subject}"

    def __sub__(self, other):
        age = self.age - other.age
        return age

#''''''''''''''''''''''''''''''''''''''''''''''
def main():
    student = Student("Harry", "Gryffindor", 20)
    professor = Professor("Amirov", "Pascal", 50)
    print(f"{student}")
    print(f"{professor}")

    print(f"{student + professor}")
    print(f"{professor - student}")

#''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()
