import tkinter as tk

def click(button_text):
    expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, expression + button_text)
    
def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Calculator")
window.geometry("300x250")


entry = tk.Entry(window, width = 20, borderwidth= 4, font=("Aerial, 14"), relief="solid")
entry.grid(row = 0, column = 0, columnspan= 4, padx = 10, pady = 10)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
    ,("C",5,0)
]


for (text, row, column) in buttons:
    if text == "C":
        button = tk.Button(window, text = text, width = 10, height = 3, command= clear)
    elif text == "=":
        button = tk.Button(window, text = text, width = 10, height = 3, command = calculate)
    else:
        button = tk.Button(window, text = text, width = 10, height = 3, command = lambda t = text: click(t))

    button.grid(row = row, column = column)

window.mainloop()




