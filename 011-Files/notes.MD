# File Handling

In python we can open a file using the built-in `open()` function which returns a file for us. 

`open()` has two main arguments that we should pass, the first is the name or path to the file we want to open. We also want to pass the mode:

    "r" - Read - Opens a file for reading
    "a" - Append - Opens a file for appending
    "w" - Write - Opens a file for writing
    "x" - Create - Create a file, if it doesn't exist

    "t" - Text Mode (read a file as text)
    "b" - Binary Mode (read a file as binary digits)

We can specify r/a/w/x and t/b at the same time. For example to open a text file in read mode:

    myFile = open("thefile.txt", "rt")

`open()` raises `OSError` exception if the file doesn't exist or the operation is otherwise invalid.

## Read Files

We can mainly read files using two built in functions `myFile.read()` and `myFile.readline()`.

An empty `myFile.read()` will just return all the contents of the file.

Alterrnatively we can read a file character by character by passing an argument

    # Read first 10 characters of myFile
    myFile.read(10)
    myFile.close()

Finally, `myFile.readline()` will read the file line by line (delimiting on newline characters `\n`)

    # Print the first line of a file
    print(myFile.readline())
    myFile.close()

The iterator for the File object is defined such that it returns each line of the file in order. So we can loop through a file line by line with `for`:

    # Print an entire file line-by-line
    for line in myFile:
      print(line)
    myFile.close()

## Create and Write to a File

To write to a file we can pass either the "a" mode to append to the end of a file, or we can pass "w" to overwrite the file.

    # Add a new line of text to the end of our example file
    myFile = open("thefile.txt", "at")
    myFile.Write("This line will be added to the end of the file")
    myFile.close()

I can also create a file by passing the "x" mode. This will throw an error if the file already exists.

    myFile = open("newfile.txt", "x")

## Deleting

We need to import the `os` module from the Python standard library. Then we can just call `os.remove("file")` on the file's path.

    import os
    os.remove("newfile.txt")

Use `os.rmdir` to remove an entire folder/directory.

## Paths