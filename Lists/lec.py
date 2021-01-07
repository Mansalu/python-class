# Lists and For Loops

# Create a list using the square bracket syntax
myList = ["apple", "cheese", "orange"]

# Add to the end of an existing list with append()
myList.append("milk")

# Get the number of items in the list with len()
print("Size of the list is", len(myList))

# Remove an item from a list
myList.remove("apple")

# Remove an item from a list by index
myList.pop(0)

print("The first two items of the list were removed")
print("The remaining items are:")

# Loop over all the items in a list and print each on its own line
for item in myList:
    print(item)

