# GUI Practice

#Simple two operator calculator.

from tkinter import *

Window = Tk()

Window.title('Simple Calculator')

Window.geometry('500x200')

LabelNumber = Label(Window, text = 'Enter a number:')
LabelNumber.grid(column =1, row = 0)
NumberBox1 = Entry(Window,width=4)
NumberBox1.grid(column =2, row=0)

LabelNumber2 = Label(Window, text = 'Enter another number:')
LabelNumber2.grid(column = 1, row = 4)
NumberBox2 = Entry(Window,width=4)
NumberBox2.grid(column =2, row=4)

Result = Label(Window,text = 'Result:')
Result.grid(column = 5, row = 1)

def MultiplyButtonClick():
    FloatNumberBox1 = float(NumberBox1.get())
    FLoatNumberBox2 = float(NumberBox2.get())
    OutputNumber = FloatNumberBox1 * FLoatNumberBox2
    OutputString = 'Result: ' + str(OutputNumber)
    Result.configure(text = OutputString) 

MultiplyButton = Button(Window,text = 'Multiply', command = MultiplyButtonClick)

MultiplyButton.grid(column = 2, row = 5)

def AddButtonClick():
    FloatNumberBox1 = float(NumberBox1.get())
    FLoatNumberBox2 = float(NumberBox2.get())
    OutputNumber = FloatNumberBox1 + FLoatNumberBox2
    OutputString = 'Result: ' + str(OutputNumber)
    Result.configure(text = OutputString)

AddButton = Button(Window, text = 'Add',command = AddButtonClick)

AddButton.grid(column = 2, row = 6)

def SubtractButtonClick():
    FloatNumberBox1 = float(NumberBox1.get())
    FLoatNumberBox2 = float(NumberBox2.get())
    OutputNumber = FloatNumberBox1 - FLoatNumberBox2
    OutputString = 'Result: ' + str(OutputNumber)
    Result.configure(text = OutputString)

SubtractButton = Button(Window, text = 'Subtract',command = SubtractButtonClick)

SubtractButton.grid(column = 4, row = 6)

def DivideButtonClick():
    FloatNumberBox1 = float(NumberBox1.get())
    FLoatNumberBox2 = float(NumberBox2.get())
    OutputNumber = FloatNumberBox1 / FLoatNumberBox2
    OutputString = 'Result: ' + str(OutputNumber)
    Result.configure(text = OutputString)

DivideButton = Button(Window, text = 'Divide',command = DivideButtonClick)

DivideButton.grid(column = 4, row = 5)

Window.mainloop()
