class Animal:
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meaw(self):
        print("Cat meows")

class Cow(Animal):
    def moo(self):
        print("Cow moos")

dog = Dog()
dog.speak() # From Animal
dog.bark() # From Dog

cat = Cat()
cat.speak() # From Animal
cat.meaw() # From Cat

