# File reading
# Read in the contents of the file from part 1
# Gather all the temps in either C or F (not both)
# Don't forget to close the file
# Print to the console conversions in K

# What can go wrong? (file doesn't exist....anything else?)

File2 = open('CFK.txt', 'rt')
FileContent = File2.read()
File2.close()
FileLines = FileContent.split("\n")
FileLines.pop(0)
KelvinValues = []
for line in FileLines:
    val = line.split("\t")[2]
    KelvinValues.append(val)
print(KelvinValues)
