#Problem statement: Write a program to print sum of n natural numbers using recursion.


def sum(number):
    if(number==1):
        return 1
    else:
        return number+sum(number-1)
    
n=int(input("Enter number: "))
answer=sum(n)
print(f"Sum is: {answer}")