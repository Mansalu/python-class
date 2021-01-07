# Lists and For Loops

A list is a collection which is ordered and mutable. A list allows duplicates. Lists are created
using square brackets `[]`

## Define a list

    myList = ["apple", "banana", "orange"]

Printing a list is easy in Python

    print(myList)

## Index

Lists are ordered, and items in a list can be accessed by the index.
Lists are 0 indexed, meaning they begin at 0. We can print a specific
item from the list above:

    print(myList[1])

In this case "banana" is printed.

List items can also be changed by index

    myList[2] = "milk"

This code changes the last item in the list to be "milk" instead of "orange"

## List Length

The length of a list can be determined with the built in `len()` function.

    listLength = len(myList)

Using the list from the example above `listLength` is 3.

## Append

You can add to an existing list with the built in `append()` function.

    myList.append("cheese")

Will add a 4th item "cheese" to our existing list.

## Remove and Pop

You can remove items from a list using the built in `pop()` and `remove()` functions.

Remove an item from a list by value

    myList.remove("banana")

Or by index

    myList.pop(1)

For our existing list, the result here is the same. The list item "banana" will be removed.

## For loops in Python

A for loop is another type of loop in Python, similar to while, it is used to execute a block of
code numerous times. For loops are most commonly used to loop over the items in a collection.

For example, we want to answer the question: Is "milk" on the list?

    for item in myList
        if (item == "milk")
            print("Found Milk")


    