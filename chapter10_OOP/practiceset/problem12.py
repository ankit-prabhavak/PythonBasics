class Admission:

    __student_id = None
    __marks = None
    __age = None

    def __init__(self, student_id, marks, age):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age


    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False
            

    def validate_age(self):
        if self.age >= 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.__marks >= 65:
            return True
        else:
            False

    def getter(self):
        return (self.__student_id, self.__marks, self.__age)

    def setter(self, id, marks, age):
        self.__student_id = id
        self.__marks = marks
        self.__age = age
