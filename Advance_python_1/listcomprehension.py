mylist = [1, 2, 3, 5, 3, 6, 9]



squaredlist=[]

# for item in mylist:
#     squaredlist.append(item*item)

squaredlist = [i*i for i in mylist]
print(squaredlist)