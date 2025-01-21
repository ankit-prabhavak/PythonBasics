#Function:

#Function definition
def average():
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    c=int(input("Enter number 3: "))

    average=(a+b+c)/3
    print(f"Average: {average}")


n=int(input("Enter n: "))

for i in range(1,n+1):
    average()   #Function call
   