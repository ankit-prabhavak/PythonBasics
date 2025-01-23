def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage
str1 = input("Enter the first word/phrase: ")
str2 = input("Enter the second word/phrase: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
