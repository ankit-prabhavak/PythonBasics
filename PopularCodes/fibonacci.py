def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
print("Fibonacci sequence for 10 numbers:")
for i in range(10):
    print(fibonacci(i), end=' ')