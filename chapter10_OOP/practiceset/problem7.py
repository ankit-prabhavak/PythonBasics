class Student:
    
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english


    def calculate_average(self):
        return (self.maths + self.science + self.english) / 3
    

student1 = Student("Ankit", 90, 85, 95)
print(student1.calculate_average())  # Output: 90.0

student2 = Student("Anmol", 96, 80, 81)
print(round(student2.calculate_average()))  # Output: 86


