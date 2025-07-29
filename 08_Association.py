class School:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, school):
        self.name = name
        self.school = school  # Association

    def show_info(self):
        print(f"{self.name} works at {self.school.name}")

# ব্যবহার:
s1 = School("Oxford International School")
t1 = Teacher("Mr. Karim", s1)

t1.show_info()
