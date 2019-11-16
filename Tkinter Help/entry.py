from tkinter import *

root = Tk()

e= Entry(root, width=50, borderwidth=7)
e.pack()
e.get()
e.insert(0, "Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()


myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick, fg="white", bg="black")
myButton.pack()



root.mainloop()