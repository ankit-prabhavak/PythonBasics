#Problem Statement: Write a program to print greatest among the three numbers.


def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))

answer=greatest(a,b,c)
print(f"Greatest among the three is: {answer}")