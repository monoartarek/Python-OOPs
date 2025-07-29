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


#double underscore (need setter method to change it you cant change it directly)------------------------>


# class Student:
#     def __init__(self, name):
#         self.__name = name

#     def getter(self):
#         return self.__name

# s1 = Student("Tarek")
# print(s1.getter())  # Output: Tarek

# # WRONG attempt to change private variable
# s1.__name = "Monoar"
# print(s1.getter())  # Still outputs: Tarek



#single underscore(you can change it directly)-------------------------->

# class Student:
#     def __init__(self, name):
#         self._name = name

# s1 = Student("Tarek")
# s1._name = "Monoar"  # ✅ This works
# print(s1._name)      # Output: Monoar
