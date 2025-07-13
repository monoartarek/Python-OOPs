#class 1
class Doctor:
    def treat(self, patient):
        print(f"Doctor is treating {patient.name}")

#class 2
class Patient:
    def __init__(self, name):
        self.name = name

p = Patient("Rahim")
d = Doctor()
d.treat(p) # Association: just object pass korlam


