import matplotlib.pyplot as plt
import numpy as np


# Question 1:
Food  = ['Meat', 'Banana', 'Avocados', 'Sweet Potatos', 'Spinach', 'Watermelon','Coconut water', 'Beans', 'Legumes' , 'Tomato']
Calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
Potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
Fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]


# Plotting the data
plt.plot(Food, Calories, label='Calories', marker='o')
plt.plot(Food, Potassium, label='Potassium', marker = 'o')
plt.plot(Food, Fat, label='Fat', marker = 'o')


plt.xlabel('Food')
plt.ylabel('Nutrients\n(Calories, Potassium, Fat)')

plt.title('Food vs Nutrients (Calories, Potassium, Fat)')

plt.grid()
plt.legend()
plt.show()



# Question 2:
# import matplotlib.pyplot as plt
# import numpy as np
# month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novemver", "December"]
# houseA = [8, 9, 7, 15, 6, 3, 12, 15, 48, 75, 11, 13]
# houseB = [15, 4, 8, 10, 15, 11, 8, 4, 9, 8, 14, 6]
# colour = ["red","blue","orange","green","yellow","lime","skyblue","magenta","grey","pink","indigo"]
# p = np.arange(len(month))

# plt.bar(p - 0.2,houseA, label="House A" ,color="orange",alpha = 1, edgecolor="black",width=0.4)
# plt.bar(p + 0.2,houseB, label="House B" ,color="green",alpha = 1, edgecolor="black",width=0.4)

# plt.xlabel('Months of the year',fontsize=8,fontweight="bold",fontstyle=None)
# plt.xticks(p,month)
# plt.ylabel('Power consumed by House A\n(in kwh)',fontsize=8,fontweight="bold",fontstyle=None)
# plt.title("Power consumption of House A over the year",fontsize=10,fontweight="bold",fontstyle=None)

# plt.legend()
# plt.show()


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



# 1. Slicing:
# Slicing is a technique used to extract a portion of a list (or other sequence types, such as strings or tuples). It allows you to get a sublist by specifying a start, stop, and step.

# Syntax:

# python
# Copy
# sequence[start:stop:step]
# start: The index from where the slicing starts (inclusive).
# stop: The index where the slicing ends (exclusive).
# step: The step or interval between indices (optional).
# If any of these are omitted, they take default values:

# start defaults to 0.
# stop defaults to the length of the sequence.
# step defaults to 1.
# Example:
# python
# Copy
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slicing: Extracts elements from index 2 to 5 (exclusive of 5)
# sublist = my_list[2:5]  
# print(sublist)  # Output: [2, 3, 4]

# # Slicing with step: Extracts elements from index 1 to 8, with step of 2
# sublist_step = my_list[1:8:2]  
# print(sublist_step)  # Output: [1, 3, 5, 7]

# # Omitting start, stop, and step
# sublist_full = my_list[:]  
# print(sublist_full)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2. List Comprehension:
# List comprehension provides a concise way to create lists by iterating over an iterable (like a list, range, or string) and applying an expression to each item.

# Syntax:

# python
# Copy
# [expression for item in iterable if condition]
# expression: The value or operation that you want to compute for each item.
# item: The variable that represents each element of the iterable.
# iterable: The sequence you are looping through (e.g., a list or range).
# condition (optional): A condition to filter items in the iterable.
# Example:
# python
# Copy
# # List comprehension to create a list of squares
# squares = [x**2 for x in range(5)]
# print(squares)  # Output: [0, 1, 4, 9, 16]

# # List comprehension with condition: Get even numbers
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# # List comprehension with a more complex expression
# strings = ["hello", "world"]
# uppercase_strings = [s.upper() for s in strings]
# print(uppercase_strings)  # Output: ['HELLO', 'WORLD']
# Benefits of List Comprehension:
# Concise: One-liner way to create lists.
# Readable: Often clearer than using loops.
# Efficient: Faster than using loops for list creation due to the internal optimizations.
# Summary:
# Slicing is used to extract portions of a sequence based on indices and steps.
# List comprehension is a concise way to generate a new list by iterating over an existing iterable and applying an expression or condition.



import random

def code_of_the_day():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Talk is cheap. Show me the code. – Linus Torvalds",
        "Code is like humor. When you have to explain it, it’s bad. – Cory House",
        "First, solve the problem. Then, write the code. – John Johnson",
        "Simplicity is the soul of efficiency. – Austin Freeman",
        "In programming, the hard part isn’t solving problems, but deciding what problems to solve. – Paul Graham",
        "It’s not a bug, it’s an undocumented feature. – Anonymous",
        "There are only two hard things in computer science: cache invalidation and naming things. – Phil Karlton"
    ]
    
    # Randomly select a quote from the list
    return random.choice(quotes)

# Print the code of the day
print("Code of the Day:")
print(code_of_the_day())
