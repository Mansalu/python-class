# File writing
# Prompt the user for 3 parameters
# Start, End, Step {0...100, 5}
# Make a file called Temps.txt and write two columns of C to F conversions (see sample file)
# Write each conversion from Start to End in increments of Step
# Close the file (report success on the console)

TempStartCelsius = int(input('Enter start index in celsius: '))
TempEndCelsius = int(input('Enter end index in celsius: '))
TempStepCelsius = int(input('Enter the step you want to increment the temperature by: '))

print('Celsius')

MyFile = open('CFK.txt','xt')

while (TempStartCelsius<TempEndCelsius):
    TempStartCelsius += TempStepCelsius 
    ColumnCelsius = MyFile.write(str(TempStartCelsius))
    RowToColumn =  
    print(TempStartCelsius)


    

    
