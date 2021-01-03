# While Loops -- FizzBuzz

"""
Count from 1 to 100, printing the current count. However, if the count is
a multiple of 3, print "Fizz" instead of the count. If the count is a
multiple of 5 print "Buzz" instead. Finally, if the count is a multiple of both print 
"FizzBuzz" instead.

Example
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
"""
#Intro
print("This is a FizzBuzz game.")
#Defining Count and Limit for Fizz Buzz.
Count = 0
Limit = 100
# Running while loop of count from 0 to 100 in increments of 1.
while (Count < Limit):
    Count += 1
    # If Count is divisible by 5 and 3 then the program prints Fizz Buzz.
    if (Count % 5 == 0 and Count % 3 == 0 ):
        print ("Fizz Buzz")
    # Else if the previous condition is not satisfied, 
    # then check if count is divisible by 5 then print Buzz if it is.
    elif (Count % 5 == 0):
        print ("Buzz")
    elif (Count % 3 == 0):
        print("Fizz")
    # If none of these conditions are satisfied then the count is printed.
    else:
        print (Count)

print ("END OF FIZZ BUZZ")
 # END

    
