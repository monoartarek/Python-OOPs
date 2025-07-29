#✅ With @property decorator the gettr and setter method will more (clean & Pythonic):
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):           # Acts like a getter
        return self.__name

    @name.setter
    def name(self, value):    # Acts like a setter
        self.__name = value

s1 = Student("Tarek")
print(s1.name)          # Looks like attribute, but calls getter (without parentheses)
s1.name = "Monoar"      # Looks like setting attribute, but calls setter
print(s1.name)

