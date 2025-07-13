class Exam:
    school = "Naogaon High School"

    @staticmethod
    def calculate_grade(marks):
        if marks >= 33:
            return "Passed"
        else:
            return "Fail"
    
print(Exam.calculate_grade(35))