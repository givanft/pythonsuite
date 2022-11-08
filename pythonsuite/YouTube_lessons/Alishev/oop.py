#---------------------------------------
class Person:
    
    def __init__(self, name: str, surname: str, year_of_birth: int) -> None:
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
    
    # GETTERs ----------------------------------------
    @property # get NAME
    def name(self) -> str:
        return self._name
    @property # get SURNAME
    def surname(self) -> str:
        return self._surname
    @property # get YEAR OF BIRTH
    def year_of_birth(self) -> int:
        return self._year_of_birth

    # SETTERs ---------------------------------------
    @name.setter
    def name(self, n: str) -> None:
        if len(n) <= 0:
            raise ValueError("Invalid Name")
        self._name = n
    @surname.setter
    def surname(self, sn: str) -> None:
        if len(sn) <= 0:
            raise ValueError("Invalid Surname")
        self._surname = sn
    @year_of_birth.setter
    def year_of_birth(self, byear: int) -> None:
        if byear <= 0:
            raise ValueError("Invalid Year Of Birth")
        self._year_of_birth = byear



    def __str__(self) -> str:
        return f"Name: {self._name} {self._surname}, year: {self._year_of_birth}"

    def __del__(self) -> None:
        pass
#---------------------------------------

ivan = Person("Ivan", "Gorsh", 500)
katy = Person("Katya", "Sypricheva", 1982)

print(f"{katy}\n{ivan}")
