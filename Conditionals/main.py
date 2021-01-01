# Conditions -- Number Knowledge
print("This is a number knowledge program.")

print("Enter a number to find out if it is negative, positive, or zero and even or odd.")

UserNumber = input("Enter a number: ")

if(int(UserNumber) == 0):
    print("The number is zero.")
elif (int(UserNumber) > 0):
    print("The number is positive.")
else :
    print("The number is negative.")


if (int(UserNumber) % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

