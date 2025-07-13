class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name

class University:
    def __init__(self, uni_name, department):
        self.uni_name = uni_name
        self.department = department # Aggregation 

    def show_info(self):
        print(f"{self.uni_name} has the {self.department.dept_name} department")

#create a Department object 
d1 = Department("Computer Science")

#pass Department into University (Aggregation)
u1 = University("Dhaka University", d1)

#show details 
u1.show_info()