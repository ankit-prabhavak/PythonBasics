def is_leap_year(year):
    # Check if the year is divisible by 4, but not divisible by 100, unless it is divisible by 400
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Input year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year using the function
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
