## What is a class?

## What is the role of the constructor?

## The following code produces a stack trace. How can we fix this so that the variable 7 is printed?

    class MyClass:
        def __init__(self):
            self.variable = 7
    
    print(MyClass.variable)

## Consider the following code. What is the difference between MyClass and myClass?

    class MyClass:
        def __init__(self, var)
            self.var = var
            
    myClass = MyClass(10)