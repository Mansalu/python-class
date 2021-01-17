# GUI Programming -- Tkinter
from tkinter import *

def ButtonClicked():
    outputString = "Hello " + textBox.get()
    outLabel.configure(text=outputString)

Form = Tk()
Form.title('First Application')
Form.geometry('350x200')
theLabel = Label(Form, text="Enter your first name:")
theLabel.grid()
textBox = Entry(Form, width=10)
textBox.grid(column=1, row=0)
theButton = Button(Form, text="Click Me", command=ButtonClicked)
theButton.grid(column=2, row=0)
outLabel = Label(Form)
outLabel.grid()
Form.mainloop()
