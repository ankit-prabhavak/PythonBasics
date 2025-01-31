import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Generate a key for encryption (Only needs to be done once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the secret key from the file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# Save the password into a file
def save_password(service, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{encrypted_password.decode()}\n")

# View passwords (decrypt and display)
def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file.readlines():
                service, encrypted_password = line.strip().split(":")
                decrypted_password = decrypt_password(encrypted_password.encode())
                messagebox.showinfo(service, f"Password: {decrypted_password}")
    except FileNotFoundError:
        messagebox.showwarning("No Data", "No passwords saved yet.")

# Add password function
def add_password():
    service = service_entry.get()
    password = password_entry.get()
    if service and password:
        save_password(service, password)
        messagebox.showinfo("Success", f"Password for {service} added successfully!")
        service_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Initialize the key if it does not exist
if not os.path.exists("secret.key"):
    generate_key()

# Create the main window
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x400")

# Create the label
label = tk.Label(root, text="Password Manager", font=("Arial", 16))
label.pack(pady=10)

# Create entry widgets
service_label = tk.Label(root, text="Service", font=("Arial", 12))
service_label.pack(pady=5)
service_entry = tk.Entry(root, font=("Arial", 12), width=30)
service_entry.pack(pady=5)

password_label = tk.Label(root, text="Password", font=("Arial", 12))
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), width=30, show="*")
password_entry.pack(pady=5)

# Add password button
add_button = tk.Button(root, text="Add Password", font=("Arial", 12), command=add_password)
add_button.pack(pady=10)

# View passwords button
view_button = tk.Button(root, text="View Passwords", font=("Arial", 12), command=view_passwords)
view_button.pack(pady=10)

# Run the main event loop
root.mainloop()
