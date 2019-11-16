from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("TimeForIcons")
root.iconbitmap("c:/gui/images/calculator.ico")

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="This is Frame Button")
b2 = Button(frame, text="This is also Frame Button")
b.grid(row=0, column=0)
b2.grid(row=1,column=1)




root.mainloop()
