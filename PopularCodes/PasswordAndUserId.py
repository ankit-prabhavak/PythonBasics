import random
import string

# Function to generate User ID
def generate_user_id(prefix="user", length=5):
    # Generate a random number to append to the prefix
    random_number = ''.join(random.choices(string.digits, k=length))
    user_id = prefix + random_number
    return user_id

# Function to generate Password
def generate_password(length=8):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting random characters
    password = ''.join(random.choices(characters, k=length))
    return password

# Example Usage
user_id = generate_user_id()  # You can change the length if needed
password = generate_password()  # You can change the length if needed

print("User ID:", user_id)
print("Password:", password)
