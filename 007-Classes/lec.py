# Classes and Objects (Fundamentals of Object Oriented Programming)

# Create a class with the class keyword
class Student:

    # Property for keeping track of the list of courses a student is enrolled
    EnrolledCourses = []

    # Every class needs a constructor always defined as __init__
    def __init__(self, name, GPA, major):
        self.name = name
        self.GPA = GPA
        self.major = major
    
    # Methods in a class must always accept the 'self' parameter
    # A reference to the actual object
    def EnrollInCourse(self, Course):
        self.EnrolledCourses.append(Course)

    # Another student method for attending a give course
    def AttendCourse(self, Course):
        if (self.EnrolledCourses.__contains__(Course)):
            print("Went to class")
        else:
            print("Not enrolled in", Course)

# Using my student class by creating an instance called john
john = Student("John", 4.0, "Biology")
print(john.EnrolledCourses)
john.EnrollInCourse("Introduction to Biology Fundamentals")
john.EnrollInCourse("Freshman Writing")
print(john.EnrolledCourses)
john.AttendCourse("Introduction to Biology Fundamentals")
