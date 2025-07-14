class Grandfather:
    def legacy(self):
        print("Grandfather's legacy")

class Father(Grandfather):
    def work(self):
        print("Father's Profession")

class Son(Father):
    def study(self):
        print("Son is studying")

obj = Son()
obj.legacy() # From Grandfather class
obj.work() # From Father class
obj.study() # From Son class

