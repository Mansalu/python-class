# File writing
# Prompt the user for 3 parameters
# Start, End, Step {0...100, 5}
# Make a file called Temps.txt and write two columns of C to F conversions (see sample file)
# Write each conversion from Start to End in increments of Step
# Close the file (report success on the console)

#Getting user input for Start, End, and Step in celsius.
TempStartCelsius = int(input('Enter start index in celsius: '))
TempEndCelsius = int(input('Enter end index in celsius: '))
TempStepCelsius = int(input('Enter the step you want to increment the temperature by: '))

# Try this code to catch FileExistsError. 
try:
    # Creating and Opening a new file. 
    MyFile = open('CFK.txt', 'xt')
    MyFileHeaders = MyFile.write('C' + '\t' + 'F' + '\t' + ' K')

    # Sets condition for while loop less than or equal to TempEnd
    while (TempStartCelsius < TempEndCelsius or TempStartCelsius == TempEndCelsius):
        CelsiustoFahrenheit = ((9/5)*int(TempStartCelsius)) + 32
        CelsiustoKelvin = int(TempStartCelsius) + 273.15
        # Writing each row to file for TempStart plus TempStep
        FileWrite = MyFile.write('\n' + str(TempStartCelsius) + '\t' + str(CelsiustoFahrenheit) + '\t' + str(CelsiustoKelvin))
        # Creates increment. 
        TempStartCelsius += TempStepCelsius
    MyFile.close()
# If FileExistsError occurs 'File Already Exists is printed'. 
except FileExistsError:
    print('File Already Exists')






    




    

    
