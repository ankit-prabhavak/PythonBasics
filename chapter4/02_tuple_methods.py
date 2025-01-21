# a= (20,"Ankit",21,"Aditya")

# no=a.count(20)
# print(no)
# i=a.index("Ankit")
# print(i)
tuple=(1,2,3)

repeated=tuple*3
print(repeated)

print(type(repeated))

#membership using 'in' keyword.
print(2 in repeated)

print(len(repeated))

sliced=repeated[1:4]
print(sliced)

#unpacking
a,b,c=tuple
print(a,b,c)