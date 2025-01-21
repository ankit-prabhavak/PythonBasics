def divide(n):
    if n%5==0:
        return True
    return False


l = [545665,222,4545,785,1020,2236]

s = list(filter(divide, l))

print(s)