def factorial(n):
    # Initialize result as 1 (since factorial of 0 is 1)
    result = 1
    
    # Multiply result by each number from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    return result

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}.")
