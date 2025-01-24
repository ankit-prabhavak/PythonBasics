import random
import string

# Function to generate password with customizable components
def generate_custom_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    # Ensure there's enough character set to build the password
    if not chars:
        print("You must select at least one character type for the password.")
        return None
    
    password = ''.join(random.choices(chars, k=length))
    return password

# Example Usage
custom_password = generate_custom_password(length=14, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
print("Custom Password:", custom_password)
