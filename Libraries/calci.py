# from tkinter import *
# import math

# root = Tk()
# root.title('SimpleCalculator')
# root.geometry('290x520')
# root.resizable(0,0)
# root.config(bg='skyblue')


# expression = ""

# def update_display():
#     rom.config(text=expression)

# def getDigit(op):
#     global expression
#     expression += str(op)
#     update_display()


# def performOperation(op):
#     global expression
#     expression += str(op)
#     update_display()


# def calculate():
#     global expression
#     try:
#         expression = str(eval(expression))  
#     except Exception as e:
#         expression = "Error"  
#     update_display()


# def clear_expression():
#     global expression
#     expression = ""
#     update_display()


# def clear_last_char():
#     global expression
#     expression = expression[:-1]
#     update_display()


# def percentage():
#     global expression
#     try:
#         expression = str(float(expression) / 100)
#     except Exception as e:
#         expression = "Error"
#     update_display()

# def SquareRoot():
#     global expression
#     try:
#         expression = str(float(expression) ** 0.5)
#     except Exception as e:
#         expression = "Error"
#     update_display()

# def Square():
#     global expression
#     try:
#         expression = str(int(expression)**2)
#     except Exception as e:
#         expression = "Error"
#     update_display()
    

# def expo():
#     global expression
#     try:
#         expression = str(math.e**int(expression))
#     except Exception as e:
#          expression = "Error"
#     update_display()
    
    
# def fact():
#     global expression
#     try:
#         expression = str(math.factorial(int(expression)))
#     except Exception as e:
#         expression = "Error"
#     update_display()


# rom = Label(root, text='0', bg="white", fg='black')
# rom.grid(row=0, column=0, pady=20, columnspan=8, sticky='w')
# rom.config(font=('verdana', 30, 'bold'))


# b = Button(root, text="%", bg="orange", fg='black', width=9, height=4, command=percentage)
# b.grid(row=1, column=0)

# b = Button(root, text="CE", bg="blue", fg='black', width=9, height=4, command=clear_expression)
# b.grid(row=1, column=1)

# b = Button(root, text="C", bg="blue", fg='black', width=9, height=4, command=clear_expression)
# b.grid(row=1, column=2)

# b = Button(root, text="X", bg="red", fg='black', width=9, height=4, command=clear_last_char)
# b.grid(row=1, column=3)

# b = Button(root, text="7", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(7))
# b.grid(row=2, column=0)

# b = Button(root, text="8", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(8))
# b.grid(row=2, column=1)

# b = Button(root, text="9", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(9))
# b.grid(row=2, column=2)

# b = Button(root, text="/", bg="orange", fg='black', width=9, height=4, command=lambda: performOperation('/'))
# b.grid(row=2, column=3)

# b = Button(root, text="4", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(4))
# b.grid(row=3, column=0)

# b = Button(root, text="5", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(5))
# b.grid(row=3, column=1)

# b = Button(root, text="6", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(6))
# b.grid(row=3, column=2)

# b = Button(root, text="*", bg="orange", fg='black', width=9, height=4, command=lambda: performOperation('*'))
# b.grid(row=3, column=3)

# b = Button(root, text="1", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(1))
# b.grid(row=4, column=0)

# b = Button(root, text="2", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(2))
# b.grid(row=4, column=1)

# b = Button(root, text="3", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(3))
# b.grid(row=4, column=2)

# b = Button(root, text="-", bg="orange", fg='black', width=9, height=4, command=lambda: performOperation('-'))
# b.grid(row=4, column=3)

# b = Button(root, text="0", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit(0))
# b.grid(row=5, column=0)

# b = Button(root, text=".", bg="grey", fg='black', width=9, height=4, command=lambda: getDigit('.'))
# b.grid(row=5, column=1)

# b = Button(root, text="=", bg="red", fg='black', width=9, height=4, command=calculate)
# b.grid(row=5, column=2)

# b = Button(root, text="+", bg="orange", fg='black', width=9, height=4, command=lambda: performOperation('+'))
# b.grid(row=5, column=3)


# b = Button(root, text="sq", bg="orange", fg='black', width=9, height=4, command= SquareRoot)
# b.grid(row=6, column=0)


# b = Button(root, text="x^2", bg="orange", fg='black', width=9, height=4, command= Square)
# b.grid(row=6, column=1)


# b = Button(root, text="e^x", bg="orange", fg='black', width=9, height=4, command= expo )
# b.grid(row=6, column=2)


# b = Button(root, text="x!", bg="orange", fg='black', width=9, height=4, command= fact)
# b.grid(row=6, column=3)

# root.mainloop()


from tkinter import *
import math

# Create the main window
root = Tk()
root.title('Simple Calculator')
root.geometry('290x520')
root.resizable(0, 0)
root.config(bg='skyblue')

# Global expression variable
expression = ""

# Update the display function
def update_display():
    rom.config(text=expression)

# Function to append digits to the expression
def append_to_expression(op):
    global expression
    expression += str(op)
    update_display()

# Function to perform operations like +, -, *, /
def perform_operation(op):
    global expression
    expression += str(op)
    update_display()

# Function to calculate the result of the expression
def calculate():
    global expression
    try:
        expression = str(eval(expression))  # Evaluates the expression
    except Exception:
        expression = "Error"
    update_display()

# Function to clear the expression
def clear_expression():
    global expression
    expression = ""
    update_display()

# Function to clear the last character
def clear_last_char():
    global expression
    expression = expression[:-1]
    update_display()

# Function to calculate percentage
def percentage():
    global expression
    try:
        expression = str(float(expression) / 100)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate square root
def square_root():
    global expression
    try:
        expression = str(float(expression) ** 0.5)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate square
def square():
    global expression
    try:
        expression = str(float(expression) ** 2)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate exponentiation (e^x)
def exponentiation():
    global expression
    try:
        expression = str(math.e ** float(expression))
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate factorial
def factorial():
    global expression
    try:
        expression = str(math.factorial(int(expression)))
    except Exception:
        expression = "Error"
    update_display()

# Label to display the expression/result
rom = Label(root, text='0', bg="white", fg='black')
rom.grid(row=0, column=0, pady=20, columnspan=8, sticky='w')
rom.config(font=('verdana', 30, 'bold'))

# Button layout as a list of tuples (text, command)
buttons = [
    ('%', percentage), ('CE', clear_expression), ('C', clear_expression), ('X', clear_last_char),
    ('7', lambda: append_to_expression(7)), ('8', lambda: append_to_expression(8)), ('9', lambda: append_to_expression(9)), ('/', lambda: perform_operation('/')),
    ('4', lambda: append_to_expression(4)), ('5', lambda: append_to_expression(5)), ('6', lambda: append_to_expression(6)), ('*', lambda: perform_operation('*')),
    ('1', lambda: append_to_expression(1)), ('2', lambda: append_to_expression(2)), ('3', lambda: append_to_expression(3)), ('-', lambda: perform_operation('-')),
    ('0', lambda: append_to_expression(0)), ('.', lambda: append_to_expression('.')), ('=', calculate), ('+', lambda: perform_operation('+')),
    ('sq', square_root), ('x^2', square), ('e^x', exponentiation), ('x!', factorial)
]

# Create and place buttons dynamically
row, col = 1, 0
for (text, command) in buttons:
    button = Button(root, text=text, bg="orange" if text in ['%', '/', '*', '-', '+', '=', 'sq', 'x^2', 'e^x', 'x!'] else 'grey',
                    fg='black', width=9, height=4, command=command)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:  # Move to the next row after 4 columns
        col = 0
        row += 1

# Start the main loop to display the window
root.mainloop()
