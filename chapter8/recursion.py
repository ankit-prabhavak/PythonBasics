#RECURSION CONCEPT
'''
factorial(5)= 5 * 4 * 3 * 2 * 1
factorial(4)= 4 * 3 * 2 * 1
factorial(3)= 3 * 2 * 1
factorial(2)= 2 * 1
factorial(1)= 1
factorial(0)= 1


factorial(n)= n * (n-1)



'''

#Factorial using recursion.

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    

n=int(input("Enter the number: "))
print(f"Factorial= {factorial(n)}")


