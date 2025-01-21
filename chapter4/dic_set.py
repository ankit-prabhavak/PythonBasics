
sett = {1, 2, 3, 4 ,5, 5, 5 ,'f' ,'g' ,'h', 'j' ,'i' ,'k' }

print(type(sett))
# print(sett)   #duplicates are not allowed.

# print(sett[0])  #not allowed (indexing)


# for items in  sett:
#     print(items, end=" ")  #printing all items in the sett

# sett.add({5,6,7})  #we cannot pass a sett  to add method add () method takes only one item at a time.

# sett.add([4])  #we only single element. not list


sett.update({8985})
sett.remove(8985)

sett.discard('i')

# sett.pop()
# sett.clear()

del sett

# print(sett)  #this will show error as sett has  been deleted.  #TypeError: 'NoneType' object has no attribute 'pop'  #



sett = {1, 2, 3, 4 ,5, 5, 5 ,'f' ,'g' ,'h', 'j' ,'i' ,'k' }

s = {1,2,3}

# print(sett.difference(s))  this will print the element of sett which are not in s.

# s.difference_update(sett)  
# s.intersection(sett)

# s.intersection_update(sett)
# s.issuperset(sett)
# s.issubset(sett)
# s.isdisjoint(sett)

# s.symmetric_difference(sett)  #this will print the element which are in either s or
# s.symmetric_difference_update(sett)
# s.union(sett)  #this will print the element which are in either s or sett
# s.copy()  #this will print the copy of s

