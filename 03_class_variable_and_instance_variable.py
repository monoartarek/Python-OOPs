class Person:
    name = "Tarek" #class variable 

    def __init__(self, address):
        self.address = address #instance variable / object variable

#create 2 objects
person1 = Person("Faridpur")
person2 = Person("Dhaka")

print(person1.name) #access of class variable
print(person1.address) #access of instance variable 

print(person2.name) #class variable 
print(person2.address) #instance variable


#example : 02

# #class variable vs instance variable
# class Person:
#     name = "Tarek" #class variable

#     def __init__(self, address):
#         self.address = address #instance or object variable
    
#     def greet(self):
#         print(f"My name is {Person.name} and my address is {self.address}")

# person1 = Person("Faridpur") 
# person1.greet()
    