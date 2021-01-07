# Conditionals

"""
If-statements can be used to have a program make decisions
"""

# Prompt the user to enter a number, convert the input string to an int, and store that
# in a variable called 'number'
number = int(input("Enter a number: "))

# If the expression inside the parenthesis evaluates to True
# the indented code will run
if (number > 5):
    print("Number is greater than 5")

# Code that is not indented, like this, will always run
# It is not part of the if "block"
print("This code will always run")

# An if block can include multiple statements that are executed when the condition is true
if (number < 5):
    print("Multiple indented statements")
    print("Can be placed inside an if block")
    print("Like this")
# Else can be used to execute code when a condition evaluates to false
else:
    print("Number is not greater than 5")

# Finally elif can be used to check subsequent conditions if the first is not true
if (number > 5):
    print("Number greater than 5")
elif (number < 5)
    print("Number less than 5")
else:
    print("Number is equal to 5")
