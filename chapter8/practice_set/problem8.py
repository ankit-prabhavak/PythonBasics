#Problem statement: Write a python function to print multiplication table of a number.

def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i} ")
        
    
n=int(input("Enter number: "))

table(n)