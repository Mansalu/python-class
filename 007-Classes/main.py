# Classes and Objects -- Practice Contact Book Program

"""
This is the driver program for our Contact Book. It must import your custom
contact class. This program starts a command line dialog loop with the user,
which accepts commands such as {add, remove, list, info, update}.

You will absolutetly need to use functions in order to organize your program.
Consider a function which accepts a command as an argument, decides which action to take
prompts for user input, modifies the contact lists as needed, then returns to the event loop.
"""

import contactModule

# Defines ContactBook as an empty list.

ContactBook = []

print('This is the program for a Contact Book. It will create a custom contact list and store it. This program accepts commands such as {add,remove,list,info,update}. ')

def AddNewContact():
    print("Adding a new contact...(press enter to skip category)")
    # Getting contact information from program user.
    newContactFirstName = input("First Name: ")
    newContactLastName = input("Last Name: ")
    newContactPhoneNumber = input("Phone Number: ")
    newContactAddress = input("Address: ")
    newContactOrganization = input("Organization: ")
    newContactEmailAddress = input("Email Address: ")
    newContactGroup = input("Group: ")
    # Using the class 'contact' (init) from contactModule.py to create the contact . 
    theNewContact = contactModule.Contact(newContactFirstName, newContactLastName, len(ContactBook), newContactPhoneNumber, Address = newContactAddress, Organization = newContactOrganization, EmailAddress = newContactEmailAddress, Group = newContactGroup)
    # Adds the new contact to the ContactBook.
    ContactBook.append(theNewContact)

def RemoveContact():
    print("Removing a contact...")
    # Getting inputed First and Last name to be removed from user.
    FirstNameContactToBeRemoved = input('Enter the first name of the contact you want removed: ')
    LastNameContactToBeRemoved = input('Enter the last name of the contact you want removed: ')
    # Checking to see if contact to be removed is in ContactBook.
    for contact in ContactBook:
        if contact.FirstName == FirstNameContactToBeRemoved and contact.LastName == LastNameContactToBeRemoved:
            ContactBook.remove(contact)
            return



   
while (True):
    Command = input("Enter a Command (add,remove,list, info ,update): ")
    # Command is all lower case now.
    Command = Command.lower()
    # If 'add' or 'remove'is inputed by the program user the respective functions are executed.
    if (Command == "add"):
        AddNewContact()

    if (Command == "remove"):
        RemoveContact()
    # For each contact in the ContactBook print the first and last name. 
    if (Command == "list"):
        for contact in ContactBook:
            print(contact.FirstName,contact.LastName)
   
    if (Command == "info"):
        
        FirstNameInfoInput = input("Enter the first name of a contact for their contact information: ")
        LastNameInfoInput = input("Enter the last name of a contact for their contact information: ")
        
        contactFound = False
        for contact in ContactBook:
            # If the First and the Last name are in the contactBook then contact is found and info printed, otherwise it doesnt exist.
            if (contact.FirstName == FirstNameInfoInput and contact.LastName == LastNameInfoInput):
                print(contact.ToString())
                contactFound = True
        if (not contactFound):
            print('Contact does not exist.')
     

        
    if (Command == "update"):
    
        FirstNameUpdateInput = input("Enter the first name of a contact to change their contact information: ")
        LastNameUpdateInput = input("Enter the last name of a contact to change their contact information:  ")
        
        contactFound = False
        for contact in ContactBook:
            # Checking if contact exists again
            if (contact.FirstName == FirstNameUpdateInput and contact.LastName == LastNameUpdateInput):
                contactFound = True
                # Getting user input for Update Contact function.
                InputFirstName = input('First Name: ')
                InputLastName = input('Last Name: ')
                InputPhoneNumber = input('Phone Number: ')
                InputAddress = input("Address: ")
                InputOrganization = input("Organization: ")
                InputEmailAddress = input("Email Address: ")
                InputGroup = input("Group: ")
                # Executing contact.Updatedcontact with user inputed parameters. 
                contact.UpdateContact(InputFirstName,InputLastName,InputPhoneNumber,InputAddress,InputOrganization,InputEmailAddress,InputGroup)
             
        if (not contactFound):
            print('Contact does not exist.')
