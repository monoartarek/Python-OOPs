class Father: # Parent class 1
    def work(self):
        print("Father is an engineer")

class Mother: # Parent class 2
    def cook(self):
        print("Mother loves cooking")

#child inherites from both
class Child(Father, Mother): # add another class using comma for multiple inheritance
    def play(self):
        print("Child loves to play")

obj = Child()
obj.work() # inherit from Father class
obj.cook() # inherit form Mother class
obj.play() # From child

