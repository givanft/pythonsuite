import time

class Student:

    # �����������
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name

    def show(self):
        print('Hello, my name is', self.name)

    # ����������
    def __del__(self):
        print('Object destroyed')

# �������� �������
s1 = Student('Emma')
# �������� ����� ������
# ��� ������ ��������� �� ���� ������
#s2 = Student('Puma')
s1.show()

# �������� ������ s1
del s1

# ���������� �������� � ���������� �� �����������
#time.sleep(5)
#print('After sleep')
s2.show()