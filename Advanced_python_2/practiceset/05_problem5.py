from functools import reduce
def greater(a, b):
    if(a>b):
        return a
    return b





l = [545665,222,4545,785,1020,2236]

s = reduce(greater, l)



print(s)


