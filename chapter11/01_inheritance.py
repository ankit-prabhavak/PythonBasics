# Single inheritance.

class Programmer:
    company="Google"

    # def __init__(self,name,language):
    #     self.name=name
    #     self.language=language

    def show(self):
        print(f"The name of the programmer: {self.name}. Language: {self.language}")




class Employee(Programmer):
    company="Amazon"


    def show(self):
        print(f"The name of the programmer: {self.name}. Language: {self.language}")


p=Employee()
b=Programmer()
print(b.company)
print(p.company)










