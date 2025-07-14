class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    pass # Inherits everything from Animal but doesn't add anything

male_1 = Male()
male_1.eat()
