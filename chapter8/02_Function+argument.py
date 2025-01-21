#Function with argument

# def goodDay(name, ending):
#     print("Good Day, "+ name+"!")
#     print(ending)

# goodDay("Harry","Thank you.")
# goodDay("Aditya","Thank you.")
# goodDay("Ankit","Thanks.")


#Function:

#Function definition
def average():
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    c=int(input("Enter number 3: "))

    average=(a+b+c)/3
    return average


n=int(input("Enter n: "))

for i in range(1,n+1):
    a=average()   #Function call
    print(f"Average_{i}: {a}")