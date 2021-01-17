# Inheritance Assignment
# Make a shape class, generic super class, only attribute is color,
# no functions or behaviours besides string override ( __str__ ).
# Next class is circle has attributes radius, methods = area(), circumfrence.
#Class rectangle, has length and width (attributes) inherits from shape not circle,
#  has methods like area and perimeter.
#Class Right Triangle inherits from shape, has attributes two side lengths and has methods
# get hypotenuse, small angle, and large angle. Test with print statements. 

import math

# Defining Super Class shape.

class shape:
    def __init__(self,color):
        self.color = color

# New class circle within shape class with new parameter 'radius'.

class circle(shape): 
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius

    #Defining functions solveArea and circumfrence for circles. 

    def solveArea(self):
        area = math.pi*(self.radius ** 2)
        return area
    def circumfrence(self):
        circumfrence = 2*math.pi*self.radius
        return circumfrence

# Rectangle class within shape.
class rectangle(shape):
    # Adding length and width parameters.
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length = length
        self.width = width
    # Defining functions areaRectangle and perimeterRectangle.
    def areaRectangle(self):
        area = self.length*self.width
        return area
    def perimeterRectangle(self):
        perimeter = (2*self.length) + (2*self.width)
        return perimeter

# Adding new class Triangle with new parameters side1 and side2.
class triangle(shape):
    def __init__(self,color,side1,side2):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        # Defining functions hypotenuse, angle1 and angle2 for triangles.
    def hypotenuse(self):
        SideC = math.sqrt((self.side1**2)+(self.side2**2))
        return SideC
        
    def angle1(self):
        Angle1 = math.atan(self.side1/self.side2) 
        # Converting radians to degrees.
        FinalAngle1 = (Angle1*180)/math.pi
        return print(FinalAngle1 , 'degrees')

    def angle2(self):
        Angle2 = math.atan(self.side2/self.side1) 
        FinalAngle2 = (Angle2*180)/math.pi
        return print(FinalAngle2, 'degrees') 
        
   # Test Case

Mytriangle = triangle('red',3,4) 

(Mytriangle.angle2())