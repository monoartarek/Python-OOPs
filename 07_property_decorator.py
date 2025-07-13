class Student:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Marks can't be negative")
        else:
            self._marks = value

s = Student()
s.marks = 85      # Calls the setter
print(s.marks)    # Calls the getter
