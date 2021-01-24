
myFile = open("notes.MD", "rt")
myString = myFile.read()
listOfWords = myString.split(" ")
for word in listOfWords:
    print(word)