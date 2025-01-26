import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 20, 25, 10]

# Area chart
plt.fill_between(x, y1,y2, color="skyblue", alpha=0.4, label='Area 1-2')
plt.plot(x, y1, label='Line 1', marker='o')
plt.plot(x, y2, label='Line 2', marker='o')

# Labels and title
plt.xlabel('x-axis'), plt.ylabel('y-axis'), plt.title('Area Chart')


# Legend and Display
plt.legend(), plt.show()

