#Problem statement 1: Multiplication table

# n=int(input("Enter the number: "))
# print("Multiplication table:")
# for i in range(1,11):
#     print(f"{n} X {i}= {n*i}")

#Problem 2:

l=["Ankit","Aryan","Abhinav","Aman","Virat","Priyanshu"]

# for name in l:
#     if(name.startswith("A")):
#         print(f"Hello {name}")

#Problem 3:

# n=int(input("Enter the number: "))
# print("Multiplication table:")
# i=1
# while(i<11):
#     print(f"{n} X {i}= {n*i}")
#     i=i+1


#Problem 4:
#Prime number

# n=int(input("Enter a number: "))

# for i in range(2,n):
   
#     if((n%i) == 0):
#        print("Number is not prime")
#        break
# else:
#     print("Number is prime")

#Problem 5: Sum of n naturals number
# n=int(input("Enter the number: "))

# i=1
# sum=0

# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(f"Sum = {sum}")    

#Problem 6: factorial

# n=int(input("Enter the number: "))

# product=1

# for i in range(1,n+1):
#     product=product*i

# print(f"Factorial of the number is: {product}")    

#Problem 7: Star pattern

# n=int(input("Enter the number of rows: "))

# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ", end="")
#     for k in range(1,2*i):
#         print("*",end="") 
#     print("")

# just for understanding!
for i in range(1,10):
    print(i,end=" ")

#same problem with another approach
# n=int(input("Enter the number of rows: "))

# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ", end="")
#     for k in range(1,i+1):
#         print("*",end="") 
#     t=i-1
#     while(t>=1):
#         print("*",end="")
#         t=t-1      
#     print("")    


#Problem 8:

# n=int(input("Enter the number of rows: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#       print("*",end="")
      
#     print("")

# Problem 9:

# n=int(input("Enter the number of rows: "))

# for i in range(1,n+1):
#     if(i==1):
#         for j in range(1,n+1):
#             print("*",end="")
#     elif(i==n):
#         for j in range(1,n+1):
#             print("*",end="")
#     else:
#             print("*",end="")
#             print(" "*(n-2),end="")
#             print("*",end="")
#     print("")

#another approach:

# n=int(input("Enter a number: "))

# for i in range(1,n+1):
#     if((i==1)or(i==n)):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")    

# #Problem 9:
# n=int(input("Enter a number: "))

# for i in range(1,11):
#       print(f"{n} X {11-i}= {n*(11-i)}")
