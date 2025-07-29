#Singleton design pattern
#class er 1 ta object thakbe ar kono object create kora jabe na
#example : log in amader 1 bar e korte hoy or je kajgulo 1 bar e korte hoy segulote singleton design pattern follow kora hoy 
class Singleton:
    _instance = None #class variable

    def __new__(cls): #build in method
        if cls._instance is None:
            print("1st object is created pore ar kono object kaj korbe na ba create hobe na")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

ob1 = Singleton()
ob2 = Singleton()

print(ob1 is ob2)
