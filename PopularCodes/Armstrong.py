n = 153  # Change to 153 or any other 3-digit number
num = n
sum = 0

# Check Armstrong number for 3 digits
while n > 0:
    digit = n % 10
    sum += digit ** 3  # Cube the digit
    n //= 10

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
