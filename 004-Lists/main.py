# Lists and For -- ToDo List Program

# Introduction
print('This is a chore listing program.')
# How to interact with it
print('You can add or remove a chore or view the existing chores.')

# Defining chore list
ChoreList = []

# Telling users how to use the program.
print('Type Add to add an item to the list.')
print('Type Remove to remove an item from the list.')
print('Type View to view all the items on the list.')
print('Type Exit to exit the program.')

# While loop always runs unless broken with exit.
while (True) :
    # Makes user input pre-determined commands.
    UserInput = input("Enter a command [Add,Remove,View,Exit]: ")
    UserInput = UserInput.lower()
    #If their input is 'add' then it adds their item to the list.
    if (UserInput == 'add'):
        ChoreList.append(input('Enter the chore you want to add: '))
        print(ChoreList)
    # Else if their input is 'remove' the program checks if it is in the list 
    # and removes it if it is.
    elif (UserInput == 'remove'):
        ItemToBeRemoved = input('Enter the chore you want to Remove: ')
        for ListItem in ChoreList:
            if (ItemToBeRemoved == ListItem):
                ChoreList.remove(ItemToBeRemoved)   
        print(ChoreList)
    # else if they input 'view' the program views the current list.
    elif (UserInput == 'view'):
        print(ChoreList)
    # else if they input 'exit' the program is terminated.
    elif (UserInput == 'exit'):
        break
    
    
        
    
        

