# Graphical User Interface (GUI) Programming

A Graphical User Interface is a user interface that accepts input and can display output visually, as opposed to on the command line in what's called a Command Line Interface (CLI).

A GUI application is sometimes called a Desktop application, but almost every application you use is a GUI, including web, mobile apps, and games.

We will start by building graphical applications with the TKinter library included in Python's standard library. There are many powerful and uniquely suited libraries for building GUIs in Python, and you are encouraged to explore them. TKinter is general purpose, widely popular, and available within the standard library it is what I will introduce.

We can add the TKinter library to any program with

    import tkinter

Or

    import * from tkinter

## Creating the Main Window

Every desktop application needs a main window, this is where we will place widgets (buttons, textboxes, drawing panels, etc) that will make up our interface. The main window is just an object which comes from a class included in `tkinter`, and we can initialize it like so:

    MainWindow = tkinter.Tk()

We may want to customize some things about the main window such as size and title:

    MainWindow.title('First Application')
    MainWindow.geometry('350x200')

## The Event Loop

Recall that in past assignments we have created a "dialog loop" which continually prompts for user input and generally keeps the program running. Graphical User Interfaces must also run an event loop, which is responsible for keeping the form on our screen, listening for keyboard and mouse inputs, and much more.

We won't conern ourselves with the details of this loop, tkinter handles that. But we need to start the Event Loop, otherwise our program won't run.

    MainWindow.mainloop()

## Buttons

We can add buttons to our Window, which can be clicked, and trigger the program to do different things. The button is an object we create and add to the Window.

    def ButtonClicked():
        # This code runs when the button is clicked

    # Create the button
    MyButton = Button(MainWindow, text = "Click This", command = ButtonClicked)
    # Add the button to the window
    MyButton.pack()

## Labels

Labels are a simple way for our application to display some text.

    # Create a new label object which displays some text
    MyLabel = Label(MainWindow, text = "This is a label")
    # Place the label on the Window
    MyLabel.pack()
    # Change the label text later on
    MyLabel.configure(text = "Some updated text")

## Entry

An Entry or text box is a way that we can accept some user input within the form.

    # Create a new Entry object
    EntryBox = Entry(MainWindow, width=10)
    # Place the entry on the form
    EntryBox.pack()
    # Get some text out of the entry later on
    inputText = EntryBox.get()

## Arranging Widgets on the Window

There are three main ways we can arrange widgets on the Window: `pack()` `grid()` and `place()`

### pack

### grid

### place