import tkinter as tk
from tkinter import messagebox

# Function to handle the registration logic
def register_user():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    
    if not username or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        # Here, you can implement further logic like storing data in a database
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        
        messagebox.showinfo("Success", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("User Registration Form")

# Create and place labels and entries for username, email, and password
label_username = tk.Label(root, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=5)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email")
label_email.grid(row=1, column=0, padx=10, pady=5)

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password")
label_password.grid(row=2, column=0, padx=10, pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Register button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
