'''
Previous year even sem:
'''

'''
2-marks questions:
'''

'''
Important concepts:

# Example character
char = 'A'

# Get ASCII value of the character
ascii_value = ord(char)

print(f"The ASCII value of '{char}' is: {ascii_value}")

# Example ASCII value
ascii_value = 65

# Get the character corresponding to the ASCII value
char = chr(ascii_value)

print(f"The character corresponding to ASCII value {ascii_value} is: '{char}'")

'''

'''
7-marks questions:
'''

'''
1. Write a python program to read a file named and count the numbers of lines, words and characters in the file.
'''
# def count_file_info(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.readlines()  # Read all lines of the file
#             lines = len(content)  # Count the number of lines
            
#             words = 0
#             characters = 0
#             for line in content:
#                 words += len(line.split())  # Count words by splitting the line by whitespace
#                 characters += len(line)  # Count the characters in the line

#             print(f"Number of lines: {lines}")
#             print(f"Number of words: {words}")
#             print(f"Number of characters: {characters}")
    
#     except FileNotFoundError:
#         print(f"File {filename} not found")

# # Test the function with an example file
# count_file_info("text.txt")

'''
2. Write a python program to find the LCM of two numbers.
'''

# def find_lcm(num1, num2):
#     # Find the greatest common divisor (GCD) of the two numbers
#     def gcd(a, b):
#         while b != 0:
#             a, b = b, a % b
#             return a
#         # Find the LCM using the formula:
#         lcm = abs(num1 * num2) // gcd(num1, num2)
#         return lcm

# # Test the function with an example
# print(find_lcm(12, 15))  # Output: 60

'''
3. Write a program takes two strings and checks common letters in both the strings.
'''

# def common(s1,s2):
#     set1 = set(s1)
#     set2 = set(s2)

#     return set1.intersection(set2)

# # Test the function with an example
# letters  = common("Hari", "Hale")
# for letter in letters:
#     print(letter)  


'''
4. Write a python program to find the sum of all the items in a dictionary.
'''

# def sum_dict(dict):
#     return sum(dict.values())

# # Test the function with an example
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(sum_dict(dict))  # Output: 6

'''
5. Write a program which converts degree celcius to farenheit using lambda function.
'''
# celcius = [54, 6, 4, 6]
# farenheit = [(lambda x: (x*9/5)+32)(x) for x in celcius]  # Call the lambda function with 'x'

# print(farenheit)

'''
6. Write a program to read a file and capitalize the first letter of each word in the file.
'''
# with open('file.txt', 'r') as file:
#     data = file.read()
#     words = data.split()
#     capitalized_data = ' '.join(word.capitalize() for word in words)
    
# with open('file.txt', 'w') as file:
#     file.write(capitalized_data)

'''
7. Write a python program to create an array of 5 random integers between 10 and 50.
'''
# import numpy as np

# def random_array():
#     return np.random.randint(10, 50, 5)

# print(random_array())

'''
8. Write a python program to create a DataFrame from a dictionary and print it.
'''
# import pandas as pd

# data = {
#     "Name": ["Tom", "Nick", "John"],
#     "Age": [20, 21, 19],
#     "Score": [90, 85, 88]
#     }


# df = pd.DataFrame(data)
# print("DataFrame Created:")
# print(df) 

