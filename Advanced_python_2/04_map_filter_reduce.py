from functools import reduce


#map function.
#map example:

l = [1,2,3,4,5]

square = lambda x : x*x


sqrlist=map(square, l)

print(list(sqrlist))




#filter example:

def even(n):
    if n%2==0:
        return True
    return False


new= filter(even,l)

print(list(new))


# reduce example



sum = lambda a,b : a+b

print(reduce(sum, l))


