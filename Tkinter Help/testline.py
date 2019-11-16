from tkinter import *

root = Tk()
root.configure(bg="blue")
canvas = Canvas(root, width=3, height=3, borderwidth=0, highlightthickness=0, bg="black")
canvas.pack()

canvas.create_line(0,0,3,3, fill="red")
canvas.create_line(0,3,3,0, fill="red")

root.mainloop()