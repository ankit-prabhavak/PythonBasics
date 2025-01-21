
# f= open("senorita.txt")
# print(f.read())

# f.close()

#same can be done as below without using fclose and fopen

with open("senorita.txt") as f:
    print(f.read())