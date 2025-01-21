class Employee:
    a=1
    def __init__(self):
        print("Constructor of Employee.")

class Programmer(Employee):
    b=2
    def __init__(self):
        print("Constructor of Programmer.")

class Manager(Programmer, Employee):
    c=3
    def __init__(self):
        super().__init__()                #super() method.
        print("Constructor of Manager.")


e=Employee()
print(e.a)
#print(e.b)   This line will throw me an error as b is not an attribute of Employee()...

p=Programmer()
print(p.a,p.b)


m=Manager()
print(m.a,m.b,m.c)