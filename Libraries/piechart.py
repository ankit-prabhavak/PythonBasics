import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie chart example')
plt.show()