from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Questionnaire")
root.iconbitmap("c:/gui/images/calculator.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askquestion("Very Important question", "Why are you gay ?")
	Label(root, text=response).pack()
	if response == 1:
		Label(root, text="You clicked yes, you gay!").pack()
	else:
		Label(root, text="You clicked no, you gay !").pack()


Button(root, text="Click For Question", command=popup).pack()


root.mainloop()