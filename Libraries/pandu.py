import pandas as pd
import numpy as np


print("creating a series\n")
data = np.array(['Ankit', 'Aman', 'Aryan', 'Abhinav', 'Priyanshu', 'Virat'])

serial = pd.Series(data)
print(serial)

# print(serial[:5])

print("Column Dataframe:\n")
lst = ["My", "Name", "is", "Ankit", "Kumar"]
frame = pd.DataFrame(lst)

print(frame)

print("Two D dataframe:\n")

jaya = {"Name":["Somaya", "Swati", "Karuna", "Ritu", "Neha"], "Age":[19,20,20,19,20],"Kabhua":[2022,2019,2014,2014,2014],"Tenure":["Now",1,1,1,1,]}


devine = pd.DataFrame(jaya)
print(devine)


print("\n\n\n\n")
# Dealing with two colums
print(devine[['Name','Kabhua']])

# Dealing with rows
print("Dealing with rows:\n")
first = devine.loc[0]
second = devine.loc[2]

print(first)
print("\n\n")
print(second)


# There are a lot of methods we need to cover in pandas
