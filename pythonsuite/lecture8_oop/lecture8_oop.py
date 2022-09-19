#''''''''''''''''''''''''''''''''''''''''''''''
class Student:
#''''''''''''''''''''''''''''''''''''''''''''''
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Getter NAME ---------------------------------------
    @property
    def name(self):
        return self._name

# Setter NAME ---------------------------------------
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is empty")
        self._name = name

# Getter AGE ---------------------------------------
    @property
    def age(self):
        return self._age

# Setter AGE ---------------------------------------
    @age.setter
    def age(self, age):
        if not age.isnumeric():
            raise ValueError("Invalid age")
        self._age = int(age)

# str ---------------------------------------
    def __str__(self):
        return f"{self.name} is {self.age}."

# ---------------------------------------
    def isold(self):
        if self.age > 50:
            return "Old one..."
        return "Young one!"

# classmethod ---------------------------------------
    @classmethod
    def get(cls):
        name = input("Name: ")
        age = input("Age: ")
        return cls(name, age)


#''''''''''''''''''''''''''''''''''''''''''''''
def main():
    student = Student.get()
    print(f"{student} He is {student.isold()}")
    
##==============================================================================
##==============================================================================

## Return as DICT
#def main():
#    student = get_student()
#    if student["name"] == "Padma":
#        student["house"] = "Ravenclaw"
#    print(f"{student['name']} from {student['house']}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house}

## Return as LIST 
#def main():
#    student = get_student()
#    if student[0] == "Padma":
#        student[1] = "Ravenclaw"
#    print(f"{student[0]} from {student[1]}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return [name, house]

## Return as TUPLE (A tuple is a sequences of values. Unlike a list, a tuple can’t be modified.)
#def main():
#    name, house = get_student()
#    print(f"{name} from {house}")
## OR
#    student = get_student()
#    print(f"{student[0]} from {student[1]}")
#
#
#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return name, house
## OR
#   return (name, house)  # explicitly tells anyone that we are returning two values within one. 

if __name__ == "__main__":
    main()
