# Simple dictionary example

# Let's create a dictionary that maps student names to their major

# Empty dictionary
studentMajors = {}

# Let's add some students
studentMajors.update({"alice" : "Biolody"})
studentMajors.update({"bob" : "Computer Science"})
studentMajors.update({"charles" : "Mechanical Engineering"})
studentMajors.update({"amy" : "English"})

# Let's print this information
for (name,major) in studentMajors.items():
    print(name, "is a", major, "major")

# Nested Dictionary