from matplotlib import pyplot as plt


x = [4, 5, 7, 8, 9, 2, 1, 3]

y = [7, 8, 9, 5, 2, 3, 9, 4]

colors = ["red", "orange", "yellow", "green", "blue", "pink", "violet", "navy"]

fig, axs = plt.subplots(1, 2)

axs[0].hist(y, bins=5, edgecolor = "black", alpha=0.7, color="g")
axs[0].set_title('Histogram')

axs[1].bar(x, y, color = colors, edgecolor = "black")
axs[1].set_title('Bar Graph')

# plt.pie(x, labels= colors, autopct="%1.1f%%", startangle=90)
# plt.title("Pie chart")

# plt.legend(title="colors")
plt.show()




