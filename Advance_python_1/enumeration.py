l = [121 ,454 ,465,4 ,546]


index=0
for item in l:
    print(f"The item number at index {index} id {item}")
    index+=1


#this can be simplified using enumerate functon


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")



