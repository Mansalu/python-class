# Simple dictionary example

# Let's create a dictionary that maps student names to their major

# Empty dictionary
studentMajors = {}

# Let's add some students
studentMajors.update({"alice" : "Biology"})
studentMajors.update({"bob" : "Computer Science"})
studentMajors.update({"charles" : "Mechanical Engineering"})
studentMajors.update({"amy" : "English"})

# Let's print this information
for (name,major) in studentMajors.items():
    print(name, "is a", major, "major")

# Nested Dictionary

studentCourses = {}

for studentName in studentMajors.keys():
    studentCourses.update({studentName : {"cs101" : "Fundamentals of computer science", 
                                          "bio101" : "Intro Biology",
                                          "art200" : "survey of jazz"}})  

print(studentCourses["bob"])