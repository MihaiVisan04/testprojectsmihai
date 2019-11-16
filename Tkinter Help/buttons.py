from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look I Clicked A Button!")
	myLabel.grid(row=0, column=1)


myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="white", bg="black")
#myButton.pack()
myButton.grid(row=0,column=0)


root.mainloop()

