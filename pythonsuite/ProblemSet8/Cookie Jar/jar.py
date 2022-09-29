#''''''''''''''''''''''''''''''''''''''''''''''
class Jar:
#''''''''''''''''''''''''''''''''''''''''''''''
# -------------------------------------------------------
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
# -------------------------------------------------------
    def deposit(self, n):
        self.size = self.size + n
        if self.size > self.capacity:
            raise ValueError("Invalid capacity")
# -------------------------------------------------------
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Invalid capacity")
        self.size = self.size - n 
# -------------------------------------------------------
    @property
    def size(self):
        return self._size
# -------------------------------------------------------
    @property
    def capacity(self):
        return self._capacity  
# SETTERS -----------------------------
# Setter CAPACITY ---------------------------------------
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
# Setter SIZE ---------------------------------------
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Invalid capacity")
        self._size = size
# -------------------------------------------------------
    def __str__(self):
        return f"🍪" * self.size
#''''''''''''''''''''''''''''''''''''''''''''''
def main():
    cookies_jar = Jar()
    cookies_jar.deposit(5)
    print(f"{cookies_jar}")
    cookies_jar.deposit(5)
    print(f"{cookies_jar}")
    cookies_jar.withdraw(7)
    print(f"{cookies_jar}")
    cookies_jar.withdraw(7)
    print(f"{cookies_jar}")

#''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == "__main__":
    main()








