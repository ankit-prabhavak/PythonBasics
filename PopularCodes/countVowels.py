def count_vowels(s):
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    count = 0

    # Iterate through the string and count the vowels
    for char in s:
        if char in vowels:
            count += 1

    return count

# Example Usage
print(count_vowels("Hello World"))    # 3
print(count_vowels("Python"))         # 1
print(count_vowels("Programming"))    # 3
print(count_vowels("aeiou"))          # 5
