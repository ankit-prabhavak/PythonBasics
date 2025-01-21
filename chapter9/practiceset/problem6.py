#Problem statement: Write a program to find the line number.


with open("senorita.txt","r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("Miami" in line):
        print(f"Miami is present at line no.: {lineno}.")
        break
    lineno+=1