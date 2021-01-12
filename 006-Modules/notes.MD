# Modules

Modules in Python are similar to libraries in most other programming languages. A module is simply a Python file that contains Python code we want to use/include within our application. We can create our own modules as well as use modules written by other programmers.

Python includes a number of built-in modules we can use.

## Adding a module to our program

We can use the `import` statement to add an existing module to our program.

    import math
    print(math.cos(math.pi))

In the above example I import the built-in math module, then I access a function `math.cos()` and a variable `math.pi` from the imported module. Notice these definitions aren't part of my source file. The code will simply print the number `1` (the cosine of pi).