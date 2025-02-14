'''
Previous year PU question
'''


'''
2-marks questions:
1. write a program to accept multiple inputs from user in a single line.
2. Write a program to create a dictionary of cubes of odd numbers from 1 to 10.
'''

# Solution-1: Using input() function
# inputs = input("Enter multiple inputs separated by space: ").split()
# print("Entered inputs are: ", inputs)

# Solution-2: 

# Method-1: Using for loop
# def create_cubes_dict():
#     dict_cube = {}

#     for i in range(1, 11):

#         if i%2 != 0:
#             dict_cube[i] = i**3

#     return dict_cube

# print(create_cubes_dict())

# Method-2: Using dictionary comprehension
# odd_cubes = {i: i**3 for i in range(1, 11) if i%2 != 0}
# print(odd_cubes)


'''
7-marks questions:
1. Write a program to count the number of each vowels in a given string.
2. Write a program to create a user defined nested list and return the smallest list from the nested list.
3. Construct a program to get the fibonaci series upto 0 to 50.
4. Solve the tower of hanoi problem using recursion.
5. Write a python program to create a Tkinter-based login form with input fields for user id and password.
6. Write a python GUI to create three single line text-box to accept a value from the user using tkinter module.
7. Write a program to create a plot for sin(x), cos(x), log(x) and e(x) for variable x using subplot of matplotlib.
8. Construct a program to draw the scatter plot and line plot for X and Y where they are array of random 50 numbers.
9. Create a numpy array with 10 values. Apply array aggregation methods and find the output.
10. Write a program that create a detaframe with four columns and six rows. Apply head(), tail(), sample(), and info() functions and find output.
11. Write a program that ask the user to enter two numbers and display their sum. Raise an exception and handle it if a non-number value is given as input.
12. Write a program to print first line and last line of a text file. And also copy the content of one file to another file.


'''


# Solution-1: Using for loop

# def count_vowels(text):
#     vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for char in text:
#         if char.lower() in 'aeiou':
#             vowels_count[char] += 1

#     return vowels_count

# print(count_vowels("Hello World!")) 

# Solution-2: 
# def smallest_list(parent_list):
#     count_dict = {len(i): i for i in parent_list}
#     return count_dict[min(count_dict.keys())]

# nested_list = input("Enter nested list in [[1, 2], [3, 4], [5, 6]] format: ")
# nested_list = eval(nested_list)

# print(smallest_list(nested_list))


# Solution-3: Using for loop

# def fibonaci_series():
#     a = 0
#     b = 1
    
#     for i in range(50):
        
#         if i == 0:
#             print(a, end=" ")
#         elif i == 2:
#             print(b, end=" ")
#         else:
#             c = a + b
#             print(c , end=" ")
#             a = b
#             b = c

# fibonaci_series()


# Solution-4: Using recursion

# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n-1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n-1, auxiliary, target, source)

# tower_of_hanoi(3, 'A', 'C', 'B')


# Solution-5: Using Tkinter

# import tkinter as tk

# # Create the window
# window = tk.Tk()
# window.title("Login Form")
# window.geometry("300x250")

# # Define StringVar variables for storing user input
# user_id = tk.StringVar()
# password = tk.StringVar()

# # Create the labels and entry fields
# tk.Label(window, text="User ID: ").grid(row=0, column=0, padx=10, pady=10)
# tk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)

# tk.Label(window, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
# tk.Entry(window, textvariable=password, show="*").grid(row=1, column=1, padx=10, pady=10)

# # Create a Label for displaying login feedback (initially empty)
# feedback_label = tk.Label(window, text="", fg="red")
# feedback_label.grid(row=3, column=0, columnspan=2)

# # Define the function that runs when the Login button is pressed
# def on_login():
#     user_input = user_id.get()
#     password_input = password.get()
    
#     # Display feedback in the Tkinter window
#     feedback_label.config(text=f"User ID: {user_input}, Password: {password_input}")

# # Create the login button and link it to the on_login function
# tk.Button(window, text="Login", command=on_login).grid(row=2, column=1, pady=20)

# # Start the Tkinter event loop
# window.mainloop()

# Solution-6: Using Tkinter
# import tkinter as tk

# window = tk.Tk()
# window.title("User Input")
# window.geometry("300x250")

# a = tk.StringVar()
# b = tk.StringVar()
# c = tk.StringVar()

# tk.Label(window, text="Enter value 1: ").grid(row=0, column=0, padx=10, pady=10)
# tk.Entry(window, textvariable=a).grid(row=0, column=1, padx=10, pady=10)

# tk.Label(window, text="Enter value 2: ").grid(row=1, column=0, padx=10, pady=10)
# tk.Entry(window, textvariable=b).grid(row=1, column=1, padx=10, pady=10)

# tk.Label(window, text="Enter value 3: ").grid(row=2, column=0, padx=10, pady=10)
# tk.Entry(window, textvariable=c).grid(row=2, column=1, padx=10, pady=10)

# feedback_label = tk.Label(window, text="", fg="red")
# feedback_label.grid(row=3, column=0, columnspan=2)

# def on_submit():
#     feedback_label.config(text=f"Value 1: {a.get()} Value 2: {b.get()} Value 3: {c.get()}")
    

# tk.Button(window, text="Submit", command=on_submit).grid(row=4, column=1, pady=20)

# window.mainloop()


# Solution-7: Using matplotlib

# from matplotlib import pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# print(x)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.log(x)
# y4 = np.exp(x)

# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(x, y1)
# axs[0, 0].set_title('sin(x)')
# axs[0, 1].plot(x, y2)
# axs[0, 1].set_title('cos(x)')
# axs[1, 0].plot(x, y3)
# axs[1, 0].set_title('log(x)')
# axs[1, 1].plot(x, y4)
# axs[1, 1].set_title('exp(x)')
# plt.show()

# Solution-8: Using matplotlib

# from matplotlib import pyplot as plt
# import numpy as np

# x = np.random.rand(50)
# y = np.random.rand(50)

# fig, axs = plt.subplots(1,2)


# axs[0].scatter(x, y)
# axs[0].set_title('Scatter Plot')

# axs[1].plot(x, y)
# axs[1].set_title('Line Plot')


# plt.show()

# Solution-9: Using numpy

# import numpy as np

# arr = np.random.randint(1, 100, 10)
# print(arr)


# print("Sum of array: ", np.sum(arr))
# print("Mean of array: ", np.mean(arr))
# print("Max of array: ", np.max(arr))
# print("Min of array: ", np.min(arr))
# print("Standard deviation of array: ", np.std(arr))
# print("Variance of array: ", np.var(arr))
# print("Median of array: ", np.median(arr))
# print("Percentile of array: ", np.percentile(arr, 50))
# print("Unique values in array: ", np.unique(arr))


# Solution-10: Using pandas
# import pandas as pd


# data = {
#     'Name': ['John', 'Doe', 'Jane', 'Smith', 'Alex', 'Mary'],
#     'Age': [25, 30, 35, 40, 45, 50],
#     'Gender': ['M', 'M', 'F', 'M', 'M', 'F'],
#     'City': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad']
#     }

# df = pd.DataFrame(data)

# print("Head of dataframe: \n", df.head())
# print("Tail of dataframe: \n", df.tail())
# print("Sample of dataframe: \n", df.sample(n=2))
# print("Info of dataframe: \n")
# df.info()

# Solution-11: Using try-except block

# def add_numbers(number):
#     return sum(number)

# try:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     print("Sum of the numbers is: ", add_numbers([num1, num2]))

# except ValueError:
#     print("Please enter a valid number")

# finally:
#     print("Program executed successfully")

# Solution-12: Using file handling

# First method:

try:
    with open("paragraph.txt", "r") as file:
        lines = file.readlines()
        print("First line of file: ", lines[0])
        print("Last line of file: ", lines[-1])

    with open("text.txt", "w") as file:
        file.writelines(lines)
    
except FileNotFoundError:
    print("File not found")

finally:
    print("Program executed successfully")

    