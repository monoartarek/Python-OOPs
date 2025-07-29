class GrandFather:
    def greet(self):
        print("Grandfather says")

class Father(GrandFather):
    def greet(self):
        print("Father says")

class Children(Father):
    def greet(self):
        print("Children says")

gf = GrandFather()
f = Father()
c = Children()

gf.greet()
f.greet()
c.greet()