# import matplotlib.pyplot as plt
# import numpy as np


# Question 1:
# Food  = ['Meat', 'Banana', 'Avocados', 'Sweet Potatos', 'Spinach', 'Watermelon','Coconut water', 'Beans', 'Legumes' , 'Tomato']
# Calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
# Potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
# Fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]


# # Plotting the data
# plt.plot(Food, Calories, label='Calories', marker='o')
# plt.plot(Food, Potassium, label='Potassium', marker = 'o')
# plt.plot(Food, Fat, label='Fat', marker = 'o')


# plt.xlabel('Food')
# plt.ylabel('Nutrients\n(Calories, Potassium, Fat)')

# plt.title('Food vs Nutrients (Calories, Potassium, Fat)')

# plt.grid()
# plt.legend()
# plt.show()



# Question 2:
import matplotlib.pyplot as plt
import numpy as np
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemver", "December"]
houseA = [8, 9, 7, 15, 6, 3, 12, 15, 48, 75, 11, 13]
houseB = [15, 4, 8, 10, 15, 11, 8, 4, 9, 8, 14, 6]
colour = ["red","blue","orange","green","yellow","lime","skyblue","magenta","grey","pink","indigo"]
p = np.arange(len(month))

plt.bar(p - 0.2,houseA, label="House A" ,color="orange",alpha = 1, edgecolor="black",width=0.4)
plt.bar(p + 0.2,houseB, label="House B" ,color="green",alpha = 1, edgecolor="black",width=0.4)

plt.xlabel('Months of the year',fontsize=8,fontweight="bold",fontstyle=None)
plt.xticks(p,month)
plt.ylabel('Power consumed by House A\n(in kwh)',fontsize=8,fontweight="bold",fontstyle=None)
plt.title("Power consumption of House A over the year",fontsize=10,fontweight="bold",fontstyle=None)

plt.legend()
plt.show()


# import numpy as np
# c = np.arange(14,dtype=float)
# print(c)
# # print(c.size,c.dtype,c.itemsize,c.ndim,c.shape)

# a = np.array([1])
# print(a.ndim)

# print(np.ones((2,2),dtype=int))

# print(np.arange(5) + np.arange(5))

# jaya = np.arange(10)
# bachchan = np.array(10)

# print(jaya*bachchan)