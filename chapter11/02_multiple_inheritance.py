# CODE: MULTIPLE INHERITANCE.


class Programmer:
    company="Google"
    language="Python"

    def show(self):
        print(f"Programmer company: {self.company} and language: {self.language}")


class Coder:
    company="Amazon"
    language="Javascript"

    def getInfo(self):
        print(f"Coder company: {self.company} and language: {self.language}")



class Employee(Programmer,Coder):
    company="Infosys"
    language="HTML CSS"

    def details(self):
        print(f"Employee company: {self.company} and language: {self.language}")



b=Coder()
b.getInfo()

c=Programmer()
c.show()

a=Employee()
a.show()
a.getInfo()
a.details()