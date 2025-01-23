import string

def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Set of all lowercase letters
    alphabet = set(string.ascii_lowercase)

    # Set of all characters in the sentence
    sentence_set = set(char for char in sentence if char.isalpha())

    # Check if the sentence contains every letter of the alphabet
    return sentence_set == alphabet

# Example usage
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
