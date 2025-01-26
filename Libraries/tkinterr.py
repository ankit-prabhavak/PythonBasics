from tkinter import *

m = Tk()

# Use pack for all widgets
w = Canvas(m, width=800, height=600)
w.pack()

canvas_height  = 20
canvas_width = 20

y = int(canvas_height/2)
w.create_line(0, y, canvas_width, y)

m.title('Jai baba ki')

# Button with pack placement
button = Button(m, text='stop', width=25, command=m.destroy)
button.pack()

# Label and Entry with pack placement
e1 = Label(m, text="name")
e1.pack()
e1_entry = Entry(m)
e1_entry.pack()

m.mainloop()
