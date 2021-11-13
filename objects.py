class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


student = Student("Sebastian", (1, 2, 3, 4, 5, 6, 7))
print(student.name)
print(student.grades)
