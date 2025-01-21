class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer, Employee):
    c=3


e=Employee()
print(e.a)
#print(e.b)   This line will throw me an error as b is not an attribute of Employee()...

p=Programmer()
print(p.a,p.b)


m=Manager()
print(m.a,m.b,m.c)



