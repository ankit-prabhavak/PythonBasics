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



'''1. Generator Function:
A generator function is a function that contains one or more yield statements. When the function is called, it doesn’t execute immediately. Instead, it returns a generator object. The yield keyword is used to produce a value and pause the function’s execution. The function will resume from where it left off the next time the generator is called.

Example of a Generator Function:
python
Copy
def my_generator():
    yield 1
    yield 2
    yield 3

# Creating the generator object
gen = my_generator()

# Iterating over the generator
for value in gen:
    print(value)
Output:

Copy
1
2
3
When the function my_generator() is called, it returns a generator object, which can be iterated over.
Each time the yield statement is encountered, the function’s execution pauses, and the value is returned to the caller.
When the next value is needed, the function resumes execution right after the last yield.
2. Generator Expression:
A generator expression is similar to a list comprehension, but instead of returning a list, it returns a generator object. The syntax is almost the same, but you use parentheses () instead of square brackets [].

Example of a Generator Expression:
python
Copy
# Generator expression
gen_expr = (x * x for x in range(5))

# Iterating over the generator
for value in gen_expr:
    print(value)
Output:

Copy
0
1
4
9
16
The generator expression (x * x for x in range(5)) generates the square of each number from 0 to 4, one at a time.
Advantages of Generators:
Memory Efficiency: Generators only produce values on the fly, so they don’t store the entire sequence in memory. This makes them particularly useful when working with large datasets or infinite sequences.
Lazy Evaluation: You can process data as you need it, without having to compute all values at once. This can improve performance, especially when you don’t need to process all the values.
Cleaner Code: They allow you to write more concise and readable code, especially when dealing with complex sequences.
Example: Using Generators for an Infinite Sequence:
A common use case for generators is to work with infinite sequences without consuming an infinite amount of memory.

python
Copy
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

# Create the generator object
gen = infinite_numbers()

# Get the first 5 numbers from the infinite sequence
for i in range(5):
    print(next(gen))
Output:

Copy
0
1
2
3
4
In this example, the generator infinite_numbers() will keep generating numbers indefinitely. Using next(gen), we can retrieve the next value from the sequence one at a time.
Conclusion:
Generators are a powerful feature in Python for handling large or infinite sequences efficiently. They allow you to generate and iterate over data without consuming unnecessary memory, making them an essential tool for working with large datasets or streams of data'''