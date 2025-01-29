import numpy as np

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)

print(identity_matrix)

'''(a) Concept of a Set in Python and Its Characteristics:
In Python, a set is an unordered collection of unique elements. It is a built-in data type, defined by curly braces {} or using the set() function. Sets do not allow duplicate elements, and the order of the elements is not guaranteed.

Characteristics of a Set:
Unordered: The elements in a set are not stored in any particular order.
Unique Elements: A set cannot contain duplicate elements. If you try to add a duplicate element, it will not be added.
Mutable: Sets are mutable, meaning that you can add or remove elements after the set has been created.
No Indexing: Since sets are unordered, they do not support indexing, slicing, or other sequence-like behavior.
Can store heterogeneous elements: Sets can store elements of different types (integers, strings, etc.).
Adding and Removing Elements from a Set:
Adding elements: You can add elements to a set using the add() method.
Removing elements: You can remove elements using the remove() or discard() method. The difference is that remove() raises an error if the element is not found, while discard() does not.
Example:
python
Copy
# Creating a set
my_set = {1, 2, 3}

# Adding elements
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing elements
my_set.remove(2)  # Removes 2 from the set
print(my_set)  # Output: {1, 3, 4}

# Using discard() (no error if element doesn't exist)
my_set.discard(5)  # Doesn't raise an error
print(my_set)  # Output: {1, 3, 4}
(b) Lambda Functions within List Comprehension:
A lambda function in Python is an anonymous function that is defined using the lambda keyword. It can have any number of input parameters but only one expression. The expression is evaluated and returned.

Lambda functions are often used in list comprehensions or other functional programming tasks where you need a small, temporary function.

Example: Using a Lambda Function within a List Comprehension to Convert Celsius to Fahrenheit
To convert a list of temperatures from Celsius to Fahrenheit, we can use the formula: 
Fahrenheit
=
Celsius
×
9
5
+
32
Fahrenheit=Celsius× 
5
9
​
 +32

Using a lambda function within a list comprehension:

python
Copy
# List of temperatures in Celsius
celsius_temps = [0, 10, 20, 30, 40]

# Using a lambda function inside a list comprehension to convert to Fahrenheit
fahrenheit_temps = [lambda c: c * 9/5 + 32 for c in celsius_temps]

# Applying the lambda function to each Celsius temperature
fahrenheit_values = [f(c) for f, c in zip(fahrenheit_temps, celsius_temps)]

print(fahrenheit_values)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
Explanation:
The list comprehension creates a list of lambda functions that each convert a Celsius temperature to Fahrenheit.
The zip() function pairs each lambda function with the corresponding Celsius temperature in celsius_temps.
A second list comprehension is used to apply each lambda function to its corresponding temperature, and the result is stored in fahrenheit_values.
This approach demonstrates how you can use a lambda function in a list comprehension for simple transformations.







ChatGPT can make mistakes. Check important info.'''