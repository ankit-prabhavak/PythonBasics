set={1,2,3}

# emptyset=set() #don't use set={} to create an empty set as it will create an empty dictionary.
s={1,5,6,52.3,"Ankit"}
print(s,type(s))

s.add("Abhinav")
print(s,type(s))
s.add(10)
s.remove(5)
print(s)
