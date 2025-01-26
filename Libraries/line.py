# importing matplotlib module
from matplotlib import pyplot as plt

# x-axis values
x = [5, 2, 9, 4, 7]

# y-axis values
y = [10, 5, 8, 4, 2]

# function to plot
plt.plot(x, y,color = 'green', marker = 'o', linewidth=3,linestyle = 'dotted')
plt.grid()

plt.xlabel('Measuremrnt')

plt.ylabel("Jaya")

plt.title('comparison of the values')



# function to show the plot
plt.show()
