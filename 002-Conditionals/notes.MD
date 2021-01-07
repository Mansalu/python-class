# Conditionals

A condition is an expression that results in a boolean (true or false)

    5 > 3
    a == b
    True 
    False

## Comparison

We have several basic operators we can use for comparisons

    ==      Equality
    !=      Not equal
    >       Greater than
    <       Less than
    <=      Less than or equal
    >=      Greater than or equal

## Logic Operators

Python also includes several logical operators for putting condition together to make more complex conditions

    and     Both expressions must be true       (a and b) is true
    or      Either expression is true           (a or b) is true
    not     Expression is not true 

## If statements

In python we can create an if statement like this

    if (condition):
        # Do something

Python uses the ':' to open the if statement after a condition, and indentation is used to determine what statements are inside the if block

    if (condition):
        # This statement is inside of the if block
    # This statement is not inside the if block

We can use 'else' to run some different code if the condition is false

    if (condition):
        # Do something
    else:
        # Do a different thing

Else if (elif in Python) is avalable for creating multiple conditions

    if (condtion1):
        # Do something
    elif (condition2):
        # Do something different
    elif (condition3)
        # yet another different action

## Examples

    a = 5
    if (a > 3 and a < 10):
        print("a is a number between 3 and 10")