# Construct a program which accepts a sequence of words separated by whitespace
# as file input. Print the words composed of digits only.

def print_digit_words(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file and split into words
            words = file.read().split()
            
            # Iterate through the words and print only those composed of digits
            for word in words:
                if word.isdigit():
                    print(word)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with your file path
file_path = "input.txt"  # Replace with your file path
print_digit_words(file_path)


# hello 123 world 4567 89abc 1001
# 123
# 4567
# 1001


# Change all the numbers in the file to text. Construct a program for the same.
# Example:
# Given 2 integer numbers, return their product only if the product is equal to or lower
# than 10.
# And the result should be:
# Given two integer numbers, return their product only if the product is equal to or
# lower than one zero


def convert_numbers_to_text(file_path):
    num_dict = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }

    with open(file_path, 'r') as file:
        content = file.read()

    # Convert each character that is a digit to its word equivalent
    updated_content = ''.join(num_dict[char] if char.isdigit() else char for char in content)

    # Output the updated content
    print(updated_content)

# Ask for the file path and process it
file_path = input("Enter the path to the input file: ")
convert_numbers_to_text(file_path)


# Given 2 integer numbers, return their product only if the product is equal to or lower than 10.
# Given two integer numbers, return their product only if the product is equal to or lower than one zero.


'''Construct following filters:
1. Filter all the numbers
2. Filter all the strings starting with a vowel
3. Filter all the strings that contains any of the following noun: Agra,
Ramesh, Tomato, Patna.
Create a program that implements these filters to clean the text.'''

import re

# Filter 1: Remove all numbers
def filter_numbers(word):
    return not word.isdigit()

# Filter 2: Remove strings starting with a vowel
def filter_vowels(word):
    return not word[0].lower() in 'aeiou'

# Filter 3: Remove strings containing specific nouns
def filter_nouns(word):
    nouns = ['Agra', 'Ramesh', 'Tomato', 'Patna']
    return not any(noun in word for noun in nouns)

# Main function to apply all filters
def clean_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split the content into words
    words = content.split()

    # Apply all filters: numbers, vowels, and specific nouns
    filtered_words = [
        word for word in words
        if filter_numbers(word) and filter_vowels(word) and filter_nouns(word)
    ]

    # Join the filtered words back into a cleaned string
    cleaned_content = ' '.join(filtered_words)
    
    # Output the cleaned content
    print(cleaned_content)

# Ask for the file path and process it
file_path = input("Enter the path to the input file: ")
clean_text(file_path)




# Agra is a city in India. Ramesh went to Patna to buy tomatoes. I have 10 apples and 5 oranges.
# is a city in India. went to to buy apples and oranges.


'''Construct a function ret smaller(l) that returns smallest list from a nested list. If
two lists have same length then return the first list that is encountered. For
example:
ret smaller([ [ -2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6 , 7, 8, 9, 10], [11, 12, 13, 14, 15]])
returns [3,4,5]
ret smaller([ [ -2, -1, 0, 0.12, 1, 2], [‘a’, ’b’, ’c’, ’d’, 3, 4, 5], [6 , 7, 8, 9, 10], [11,
12, 13, 14, 15]]) returns [6 , 7, 8, 9, 10]'''


def ret_smaller(l):
    # Initialize the first list as the smallest list
    smallest_list = l[0]

    # Loop through the lists starting from the second list
    for sublist in l[1:]:
        # Compare the lengths of the sublists
        if len(sublist) < len(smallest_list):
            smallest_list = sublist

    # Return the smallest list
    return smallest_list

# Test cases
print(ret_smaller([ [-2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6 , 7, 8, 9, 10], [11, 12, 13, 14, 15]]))  
# Expected output: [3, 4, 5]

print(ret_smaller([ [-2, -1, 0, 0.12, 1, 2], ['a', 'b', 'c', 'd', 3, 4, 5], [6 , 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
# Expected output: [6, 7, 8, 9, 10]

'''A website requires the users to input username and password to register. Construct
a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria are
to be printed, each separated by a comma'''



def is_valid_password(password):
    # Check if the password length is between 6 and 12 characters
    if len(password) < 6 or len(password) > 12:
        return False
    
    # Flags for checking the conditions
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    # Loop through each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True
    
    # All conditions must be met
    if has_lower and has_upper and has_digit and has_special:
        return True
    return False

def check_passwords(passwords):
    # Split the input string into a list of passwords
    password_list = passwords.split(',')
    
    # Strip leading/trailing spaces from each password
    password_list = [password.strip() for password in password_list]
    
    # Filter valid passwords
    valid_passwords = [password for password in password_list if is_valid_password(password)]
    
    # Return valid passwords as a comma-separated string
    return ','.join(valid_passwords)

# Read comma-separated passwords from user input
user_input = input("Enter passwords (comma separated): ")

# Check the passwords and print the valid ones
valid_passwords = check_passwords(user_input)
print("Valid passwords:", valid_passwords)



'''Construct a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.
Suppose the following input is supplied to the program:
without, hello, bag, world
Then, the output should be:
bag, hello, without, world'''


def sort_words():
    # Accept input from the user
    user_input = input("Enter words separated by commas: ")
    
    # Split the input into a list of words (splitting by commas)
    words = user_input.split(',')
    
    # Strip any leading/trailing spaces from the words and sort them alphabetically
    words = [word.strip() for word in words]
    words.sort()
    
    # Join the sorted words back into a comma-separated string
    result = ', '.join(words)
    
    # Print the sorted words
    print("Sorted words:", result)

# Call the function to execute the program
sort_words()


'''Question 3:
'''
def removeNth(s, n):
    if n < 0 or n >= len(s):
        return "Invalid index"
    else:
       return s[:n] + s[n+1:]

# Test cases
print(removeNth("hello", 2))  # Expected output: "helo"


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

''''''
# Function to reverse each character and separate with commas
def reverse_and_comma_separate(file_path, output_path):
    # Open the input file and read the content
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Reverse each character in the content and separate with commas
    reversed_content = ','.join(reversed(content))
    
    # Write the reversed content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(reversed_content)
    
    print(f"Reversed content has been written to {output_path}")

# Example usage
input_file = 'input.txt'  # Path to your input file
output_file = 'output.txt'  # Path to your output file
reverse_and_comma_separate(input_file, output_file)





import math

# Function to check if a number is a perfect square
def check_perfect_square(n):
    # Calculate the square root of the number
    sqrt_n = math.isqrt(n)  # Using isqrt for integer square root (avoids floating-point issues)
    
    # Check if the square of the square root equals the original number
    if sqrt_n * sqrt_n == n:
        return sqrt_n
    else:
        return -1

# Example usage
number = 16  # Replace this with any number you want to check
result = check_perfect_square(number)

if result != -1:
    print(f"{number} is a perfect square! Its square root is {result}.")
else:
    print(f"{number} is not a perfect square.")


x = ['12', 'hello', 456]
x[0]*=3
x[1][1] = 'bye'
'''string object does not support item assignment'''

def count(s):
    for str in string.split():
        s = '&'.join(str)
    
    return s

print(count("Python is fun to learn."))
   