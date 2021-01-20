# GUI Practice

#Simple four operator calculator.

from tkinter import *
from tkinter import messagebox

# Creating Widnow using class Tk.

Window = Tk()

Window.title('Simple Calculator')

Window.geometry('500x200')


#Label for first number.

LabelNumber = Label(Window, text = 'Enter a number:')

#Placing Label onto the window grid.

LabelNumber.grid(column =1, row = 0)

# Creating Entry box for first number in grid.

NumberBox1 = Entry(Window,width=4)
NumberBox1.grid(column =2, row=0)

LabelNumber2 = Label(Window, text = 'Enter another number:')
LabelNumber2.grid(column = 1, row = 4)
NumberBox2 = Entry(Window,width=4)
NumberBox2.grid(column =2, row=4)

Result = Label(Window,text = 'Result:')
Result.grid(column = 5, row = 1)

# Function MultiplyButtonClick takes two numbers from the user,
# makes them into a float, then multiplies them, then changes them back into 
# a string so that it can use .configure to display the result. 

def MultiplyButtonClick():
    # Try valueError producing code.
    try:
        FloatNumberBox1 = float(NumberBox1.get())
        FLoatNumberBox2 = float(NumberBox2.get())
        OutputNumber = FloatNumberBox1 * FLoatNumberBox2
        OutputString = 'Result: ' + str(OutputNumber)
        Result.configure(text = OutputString)
    # If it happens make this error message box appear. 
    except:
        messagebox.showerror("Error",'One or more of the entires is not a number.')
        

    
# Creates Multiply Button with arguments, window, text, and command. 

MultiplyButton = Button(Window,text = 'Multiply', command = MultiplyButtonClick)

MultiplyButton.grid(column = 2, row = 5)

#Same utility as Multiply function but the two numbers are added instead.

def AddButtonClick():
     # Try valueError producing code.
    try:
        FloatNumberBox1 = float(NumberBox1.get())
        FLoatNumberBox2 = float(NumberBox2.get())
        OutputNumber = FloatNumberBox1 + FLoatNumberBox2
        OutputString = 'Result: ' + str(OutputNumber)
        Result.configure(text = OutputString)
    # If it happens make this error message box appear. 
    except:
        messagebox.showerror("Error",'One or more of the entires is not a number.')

AddButton = Button(Window, text = 'Add',command = AddButtonClick)

AddButton.grid(column = 2, row = 6)

#Same utility as Multiply function but the two numbers are subtracted instead.

def SubtractButtonClick():
     # Try valueError producing code.
    try:
        FloatNumberBox1 = float(NumberBox1.get())
        FLoatNumberBox2 = float(NumberBox2.get())
        OutputNumber = FloatNumberBox1 - FLoatNumberBox2
        OutputString = 'Result: ' + str(OutputNumber)
        Result.configure(text = OutputString)
    # If it happens make this error message box appear. 
    except:
        messagebox.showerror("Error",'One or more of the entires is not a number.')

SubtractButton = Button(Window, text = 'Subtract',command = SubtractButtonClick)

SubtractButton.grid(column = 4, row = 6)

#Same utility as Multiply function but the two numbers are divided instead.

def DivideButtonClick():
     # Try valueError producing code.
    try:
        FloatNumberBox1 = float(NumberBox1.get())
        FLoatNumberBox2 = float(NumberBox2.get())
        OutputNumber = FloatNumberBox1 / FLoatNumberBox2
        OutputString = 'Result: ' + str(OutputNumber)
        Result.configure(text = OutputString)
        
    # If it happens make this error message box appear for valueError or ZeroDivisionError. 
    except ValueError:
        messagebox.showerror("Error",'One or more of the entires is not a number.')
    except ZeroDivisionError:
        messagebox.showerror("Error", 'Unable to divide by zero.')

DivideButton = Button(Window, text = 'Divide',command = DivideButtonClick)

DivideButton.grid(column = 4, row = 5)

# Runs Loop on Tk functions, runs/maintains window operation. 

Window.mainloop()
