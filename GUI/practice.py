import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First GUI Program")
window.geometry("300x250")

# Declared the required variables
name = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
address = tk.StringVar()
user = tk.StringVar()
password = tk.StringVar()
password2 = tk.StringVar()

# Create the labels
tk.Label(window, text="Name").grid(row=0, column=0)
tk.Label(window, text="Phone").grid(row=1, column=0)
tk.Label(window, text="Email").grid(row=2, column=0)
tk.Label(window, text="Address").grid(row=3, column=0)

# Create the entry fields
tk.Entry(window, textvariable=name).grid(row=0, column=1)
tk.Entry(window, textvariable=phone).grid(row=1, column=1)
tk.Entry(window, textvariable=email).grid(row=2, column=1)
tk.Entry(window, textvariable=address).grid(row=3, column=1)

# Create the labels for the second part of the form
feed = tk.Label(window, text="", fg="red")
feed.grid(row=4, column=0, columnspan=2)

# Created match function for showing the details entered by the user
def match():
    n = name.get()
    p = phone.get()
    e = email.get()
    a = address.get()

    if n and p and e and a:
        feed.config(text=f"Entered Details:\nName: {n}\n Phone: {p}\n Email: {e}\n Address: {a}")
    else:
        feed.config(text="Please fill all fields")

# create submit button
tk.Button(window, text="Submit", bg="green", command=match).grid(row=5, column=0, columnspan=4)


# created label for the second part of the form
tk.Label(window, text="Username").grid(row=6, column=0)
tk.Label(window, text="Password").grid(row=7, column=0)
tk.Label(window, text="Confirm Password").grid(row=8, column=0)

# created entry fields for the second part of the form 
tk.Entry(window, textvariable=user).grid(row=6, column=1)
tk.Entry(window, textvariable=password, show="*").grid(row=7, column=1)
tk.Entry(window, textvariable=password2, show="*").grid(row=8, column=1)

# created label for displaying the username and errors 
feedback = tk.Label(window, text="", fg="green")
feedback.grid(row=9, column=0, columnspan=2)

# created a function for registering the user after getting entries in the respective fields
def register():
    u = user.get()
    p = password.get()
    p2 = password2.get()

    if u and p and p2 and p == p2:
        feedback.config(text=f"Registration Successful!! \n Username: {u}")
    else:
        feedback.config(text="Please fill all fields and ensure passwords match")

# created final buttons for registeration and exit
tk.Button(window, text="Register", bg="pink" ,command=register).grid(row=10, column=0, columnspan=4)
tk.Button(window, text="Close", bg="red", command=window.destroy).grid(row=10, column=1, columnspan=4)

# run the application
window.mainloop()
