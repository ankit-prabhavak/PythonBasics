import tkinter as tk

window = tk.Tk()
window.title("User Registeration Page")
window.geometry("300x250")

tk.Label(window, text="Name").grid(row=0, column = 0, padx= 10, pady=10)
tk.Label(window, text="Email").grid(row=1, column = 0, padx= 10, pady=10)
tk.Label(window, text="Password").grid(row=2, column = 0, padx=10, pady=10)

name = tk.StringVar()
email = tk.StringVar()
password = tk.StringVar()


tk.Entry(window, textvariable = name).grid(row=0, column = 1, padx= 10,pady=10)
tk.Entry(window, textvariable = email).grid(row=1, column = 1, padx= 10, pady=10)
tk.Entry(window, textvariable = password, show = "*").grid(row=2, column =1, padx=10, pady=10)


configure = tk.Label(window, text = "", fg="green")
configure.grid(row = 4, column = 1 , padx = 10, pady = 10)


def register():
    n = name.get()
    e = email.get()
    p = password.get()

    if n and e and p:
        configure.config(text=f"User Details: Name = {n}, Email = {e}, Password = {p}")
    else:
        configure.config(text="Please fill all fields", fg="red")

tk.Button(window, text ="Submit", command = register).grid(row = 5, column = 1, padx = 10, pady=10)

window.mainloop()