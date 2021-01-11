# Functions -- Bill Calculator
print('This is a Bill Calculator.')
print('This program adds sales tax to you bill and adds your pre-tax tip.')
# Defining a function CalcBill to calculate the amount owed 
# after tax and tip .
def CalcBill (Bill,Tip):
    """
    Adding a tax of 6% (.06) to the bill and
    adding the tip on the pre-taxed bill returns the total bill.
    """
    FinalBillFunction = Bill + (Bill*.06) + ((Bill) * (Tip/100))
    return FinalBillFunction
# True While loop to get 'Tip' and 'Bill' from user.
while (True):
    # Takes user bill and changes it to a float.
    UserBillInput = input("Enter your bill (before tax): ")
    UserBillInput = float(UserBillInput)
    # Takes user Tip percentage and changes it to an integer. 
    TipPercentage = input('Enter you tip percentage (example: 15): ')
    TipPercentage = int(TipPercentage)
    # Calls the function CallBill to evaluate UserBillInput and TipPercentage
    # as 'Bill' and 'Tip'.
    FinalBill = CalcBill (UserBillInput,TipPercentage)
    print (FinalBill , 'Dollars')


    
    

      

