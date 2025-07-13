class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I'm {self.name}")

    @classmethod
    def get_species(cls):
        print(f"we are {cls.species}")
    
p1 = Person("Tarek")

p1.say_hello()

p1.get_species() #class method access via object 
Person.get_species() #class method access via class



# Example : 02

# #class method vs instance method
# class Student:
#     name_of_school = "Naogaon High School" #class variable

#     def __init__(self, name, id): #constructor 
#         self.name = name #instance variable
#         self.id = id #instance variable
    
#     def introduce(self): # instance method 
#         print(f"My name is {self.name} and my id is {self.id}")

#     @classmethod
#     def school_name(cls): #class method 
#         print(f"My school name is {cls.name_of_school}")
    
# stu1 = Student("Tarek", 1683) #object 1
# stu2 = Student("sadia", 109) #object 2

# stu1.introduce() #instance method call
# stu2.introduce() #instance method call

# Student.school_name() #class method call using class name
# stu1.school_name() #class method call using object 1