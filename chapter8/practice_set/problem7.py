#Problem statement: Write a program to remove a name from a list and strip at the same time.

def remostrip(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))

    return n


l=["Sonia","Monaa","Pushpa","Paroaaaa","Gulabo","a"]

print(remostrip(l,"a"))
