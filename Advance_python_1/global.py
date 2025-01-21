a=89

def fun():
    a=3
    print(a)


print(a)
fun()


#see the difference.
def jun():
    global a
    a=3
    print(a)


print(a)
jun()




