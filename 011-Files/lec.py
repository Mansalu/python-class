
# Write to a file line by line
sampleFile = open("sampleFile.txt", "xt")
lineNumber = 0
while (lineNumber < 10):
    sampleFile.write("line\tnumber\t" + str(lineNumber) + "\n")
    lineNumber += 1
sampleFile.close()