class Student:
    def __init__(self, name):
        self.__name = name

    #Getter method
    def getter(self):
        return self.__name
    #setter method
    def setter(self, new_name):
        self.__name = new_name

s1 = Student("Tarek")

print(s1.getter())

s1.setter("Rafi")

print(s1.getter())