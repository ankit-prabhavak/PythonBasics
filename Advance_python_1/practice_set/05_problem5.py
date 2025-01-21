n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open("tab.txt","a") as f:
    f.write(f"The table of {n}: {table} \n")

