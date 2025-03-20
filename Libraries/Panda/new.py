import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv


data = {
    "Serial":[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
    "Name":["Ankit", "Ashutosh", "Nikesh", "Anku", "Gaurav", "Dhananjaya", "Satyam", "Vaibhav", "Rohit", "Dev", "Saurabh"],
    "Occupation":["CEH", "ME", "CEO", "Defence", "Tech", "Engg.", "UPSC", "Softy", "SUP", "DS", "Navy"]
}

df = pd.DataFrame(data)
# print(df)

df.to_csv("friends.csv", index=False)


info = []
last = []


try:
    with open('friends.csv', 'r') as file:
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            if len(row) < 2:
                print("There is less number of columns.\n")
                continue

            info.append(row[:-1])
            last.append(row[-1])

except FileNotFoundError:
    print("File not found.\n")


info = np.array(info)

first = info[:,0]
second = info[:, 1]
income = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20]
income = np.array(income)
income = np.sort(income)

# plotting 
fig, axs = plt.subplots(2, 3)

axs[0, 0].plot(second, first, label = "serial vs name", marker = "o")
axs[0, 0].set_title("Line plot")
axs[0, 0].set_xlabel("Name")
axs[0, 0].set_ylabel("Serial")
axs[0, 0].legend()
axs[0, 0].grid(True)




axs[0, 1].scatter(second, first, label = "serial vs name", marker = "o")
axs[0, 1].set_title("Scatter plot")
axs[0, 1].set_xlabel("Name")
axs[0, 1].set_ylabel("Serial")
axs[0, 1].legend()
axs[0, 1].grid(True)





axs[0, 2].bar(second, first, edgecolor="black", color="yellow", label = "serial vs name")
axs[0, 2].set_title("Bar Graph")
axs[0, 2].set_xlabel("Name")
axs[0, 2].set_ylabel("Serial")
axs[0, 2].legend()
axs[0, 2].grid(True)





axs[1, 0].hist(first, bins = income, color="g", edgecolor="black", label = "Serial vs Income")
axs[1, 0].set_title("Histogram")
axs[1, 0].set_xlabel("Serial")
axs[1, 0].set_ylabel("Income")
axs[1, 0].legend()






axs[1, 1].pie(first, labels = second, autopct ="%1.1f%%", startangle = 90)
axs[1, 1].set_title("Pie Chart")
# axs[1, 1].legend(title="Faltu")



axs[1, 2].fill_between(first, second, income,label = "Serial vs Name vs Income", alpha=0.4)
axs[1, 2].set_title("Area")


axs[1, 2].plot(first, second, label = "Serial vs Name",  marker = "o")

axs[1, 2].plot(income, second, label = "Income vs Name",  marker = "o")

axs[1, 2].set_xlabel("Serial")
axs[1, 2].set_ylabel("Income")
axs[1, 2].legend()
axs[1, 2].grid(True)


plt.show()


df =  pd.read_csv("friends.csv")
df.drop(df.columns[-1], axis=1, inplace=True)

df.to_csv("friends.csv", index=False)

print(last)
