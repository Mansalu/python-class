# Classes and Objects (Object-Oriented-Programming)

The class is a fundamental concept of the Object Oriented Programming paradigm. A class
is a blueprint or template used to create objects. A class defines an object's **properties** (variables),
and **methods** (behaviors). A classes' properties and methods are refered to as its **members**. A specific instance
of a class is called an **object**.

## Defining a Class

In python, a class is defined using the `class` keyword. 

    class MyClass:
        # Variables and functions

## Constructors

Every class must have a constructor. This is a special function that gets called when a class is
instantiated. It should be responsible for filling in the data for the class with specifics, atleast as
far as needed. The constructor is always defined as `__init__()` inside the class. A constructor always
takes in the `self` parameter. A reference to the specific object.

    class MyClass:
        def __init__(self, data):
            self.data = data

## Instantiating

A new instance of a class can invoked by calling its constructor. The constructor is called using the name of the class

    anObject = MyClass("some data")

## Accessing

You can access and objects data by derefrencing that instance. This example
prints the contents of `data` for the specific object instance of `MyClass`

    print(anObject.data)