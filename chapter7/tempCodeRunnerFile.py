n=int(input("Enter the number of rows: "))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*",end="") 
    t=i-1
    while(t>=1):
        print("*",end="")
        t=t-1      
    print("")  