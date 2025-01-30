import tkinter as tk

def click(button_text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Set up the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry widget for displaying the expression
entry = tk.Entry(window, width=20, font=('Arial', 14), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator
buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3),
    ('0', 4, 2), ('/', 1, 4), ('*', 2, 4),
    ('-', 3, 4), ('+', 4, 4), ('=', 4, 3),
    ('.', 4, 1), ('C', 5, 1)
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=calculate)
    elif text == "C":
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=clear)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: click(t))
    button.grid(row=row, column=col)

# Run the application
window.mainloop()
