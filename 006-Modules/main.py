# Modules -- Using Python's built in Math
# Driver Program which tests your functions defined in utilities.py
import utilities

# Quadraitc Tests
print("Testing SolveQuadratic()...")
print("x^2-5x-14=0 \t \t \t \t Correct:", utilities.SolveQuadratic(1,-5,-14)[0] == -2 
                             and utilities.SolveQuadratic(1,-5,-14)[1] == 7)

print("x^2+15x+50=0 \t \t \t \t Correct:", utilities.SolveQuadratic(1,15,50)[0] == -10 
                              and utilities.SolveQuadratic(1,15,50)[1] == -5)

print("12x^2-25x=0 \t \t \t \t Correct:", utilities.SolveQuadratic(12,-25,0)[0] == 0 
                             and utilities.SolveQuadratic(12,-25,0)[1] == (25/12))

# Circle Radius Tests
print("Testing FindCircleRadius()...")
print("Area=25 \t \t \t \t Correct:", utilities.FindCircleRadius(25) > 2.8 
                         and utilities.FindCircleRadius(25) < 2.9)
print("Area = 1000 \t \t \t \t Correct:", utilities.FindCircleRadius(1000) > 17.8
                            and  utilities.FindCircleRadius(1000) < 17.9)
print("Area = 306.9 \t \t \t \t Correct:", utilities.FindCircleRadius(306.9) > 9.8
                            and  utilities.FindCircleRadius(306.9) < 9.9)

# Right Triangle Tests
print("Testing SolveRightTriangleHypotnuse()...")
print("Triangle with leg lengths 14, 48 \t Correct:", utilities.SolveRightTriangleHypotnuse(14,48) == 50)
print("Triangle with leg lengths 21, 72 \t Correct:", utilities.SolveRightTriangleHypotnuse(21,72) == 75)
print("Triangle with leg lengths 4, 3 \t \t Correct:", utilities.SolveRightTriangleHypotnuse(4,3) == 5)

# F to C Conversion Tests
print("Testing ConvertFarenheitToCelsius()...")
print("Converting 100F to C \t \t \t Correct:", utilities.ConvertFarenheitToCelsius(100) > 37.7 and
                                          utilities.ConvertFarenheitToCelsius(100) < 37.8)
print("Converting 32F to C \t \t \t Correct:", utilities.ConvertFarenheitToCelsius(32) == 0)

