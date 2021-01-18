# Modules -- Using Python's built in Math Module by adding 'import math'

"""
Fill in the following functions such that the tests in main.py pass
"""
import math

def SolveQuadratic(a, b, c):
    """
    Function that solves a given quadratic equation for X. 
    Accepts constant coefficients a, b, and c. Returns two values
    x1 and x2, where x1 is always the smaller value of the two.
    
    Recall that a quadratic is an equation that can be reduced to the form

    0 = ax^2+bx+c

    Also recall the quadratic formula
    x = (-b +- sqrt(b^2 -4ac)) / (2a)
    """
    x2 = (-b + math.sqrt(b ** 2 -4*a*c)) / (2*a)

    x1 = (-b - math.sqrt(b ** 2 -4*a*c)) / (2*a)

    
    return x1,x2


def FindCircleRadius(area):
    """
    Finds the radius of a circle given circle's area

    Recall
    a = pi * r^2
    """

    Radius = (area/math.pi) ** (1/2)

    return Radius

def SolveRightTriangleHypotnuse(a, b):
    """
    Returns the hypotnuse of a triangle given the lengths 
    of two sides.
    """
    HypotenuseSideC = math.sqrt((a ** 2) + (b ** 2))
    return HypotenuseSideC
    
def ConvertFarenheitToCelsius(temperature):
    """
    Converts a given tempurature expressed in degrees farenheit
    and returns the tempurature expressed in degrees Celsius.

    Recall C=(5/9)(F-32)
    """
    Celsius =(5/9)* (temperature-32)
    return Celsius
