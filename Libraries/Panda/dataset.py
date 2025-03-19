import pandas as pd
import numpy as np
import csv


data = {
    "Serial":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Name":["Ankit", "Ashutosh", "Nikesh", "Anku", "Gaurav", "Dhananjaya", "Satyam", "Vaibhav", "Rohit", "Dev", "Saurabh"],
    "Occupation":["CEH", "ME", "CEO", "Defence", "Tech", "Engg.", "UPSC", "Softy", "SUP", "DS", "Navy"]
}

df = pd.DataFrame(data)
# print(df)
# df.info()
# print(df.head())

# df.drop(df.columns[-1], axis = 1, inplace= True)
# print(df)

# df["Occupation"] = ["CEH", "ME", "CEO", "Defence", "Tech", "Engg.", "UPSC", "Softy", "SUP", "DS", "Navy"]
# print(df)




# series = np.array(data["Name"])
# pf = pd.Series(series, name = "Name")

# print(pf)
# print(df)

petha = [[1,2,3],
         [4,5,6],
         [4,9]]

gf = pd.DataFrame(petha)
print(gf)



