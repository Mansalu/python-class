# While Loops

Loops can be used to execute a block or line of code multiple times. There are a few different loops
in Python. Today's topic is just on while loops. Like an if-statement, the while loop evaluates a condition. If the 'while' condition is true the block of code is executed. The loop condition is re-evaluated after executing the block of code, and if the condition is still true, the block will
be executed again.

    while (condition):
        # do something

## Infinite Loops

Some coniditions will always be true, and won't be changed by the loop itself. This
is known as an infinite loop. Sometimes an infinite loop is what we need. Other times 
we create them by accident, leading to a program that will never terminate, a common mistake.

    while (True)
        # do something

An intentional infinite loop can be used to keep a user input dialog going,
or run an event loop inside of something like a video game.

## Looping over a count

Lets say we want to print the sum of all the numbers from 1 to 100

    # Define a counter variable
    count = 0
    # Define a variable to hold the sum
    sum = 0
    # Loop as long as count is less than 100
    while (count < 100):
        # Increase the count on each iteration of the loop
        count += 1
        # Accumulation step
        sum += count

    # Once the loop breaks print the accumulation
    print("The sum of all numbers from 1 to 100 is", sum)

This will print the sum 5,050