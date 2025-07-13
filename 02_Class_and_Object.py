class Person:
    def __init__(self, name, age): # constructor 
        self.name = name #instance variable 1
        self.age = age #instance variable 2
    
    def greet(self): # method inside class
        print(f"Hello, My name is {self.name} and i am {self.age} years old.")

person1 = Person("Tarek", 23) #object 1
person2 = Person("sadia", 17) #object 2

person1.greet()
person2.greet()


    
    