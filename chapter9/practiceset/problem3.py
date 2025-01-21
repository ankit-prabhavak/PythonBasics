#Problem statment: Write a program to write table from 2 to 20 in a file 

def table(n):
    table= ""
    for i in range(1,11):
        table+=f"{n} X {i}= {n*i}\n"

        with open(f"tables/table_{n}.txt","w") as f:
            f.write(table)


for i in range(2,21):
    table(i)