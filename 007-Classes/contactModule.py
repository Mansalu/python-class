# Custom Class Definition for Storing a Contact

"""
A contact must have a first and last name, id number (internal), a phone number
Optionally, a contact may also have an home address, organization, e-mail address,
and a group.

For convenience, it would be wise to include a ToString() method which formats
all the details of a contact into a single string. Example:

"FirstName + LastName\n Phone: phoneNumber\n Address: addr\n Organization: org\n E-Mail Address: email\n Group: group\n"
"""

# Creating a class under Contact.
class Contact:
    # Defining the class and its base function parameters.
    def __init__(self,FirstName,LastName,IDNumber,PhoneNumber,Address = '',Organization = '',EmailAddress  = '',Group = ''):
        # Creating class variables.
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.PhoneNumber = PhoneNumber
        self.Address = Address
        self.Organization = Organization
        self.EmailAddress = EmailAddress
        self.Group = Group
    # Creating ToString function that returns the class variables vertically and seperated.
    def ToString(self):
        return "" + self.FirstName + " " + self.LastName + '\n' + 'Phone: ' + self.PhoneNumber + '\n'+ 'Address: ' + self.Address + '\n'+ 'Organization: ' + self.Organization + '\n'+ 'Email Address: ' +  self.EmailAddress + '\n'+ 'Group: ' + self.Group 
    # Default empty string to change at will.
    def UpdateContact(self, FirstName, LastName, PhoneNumber, Address, Organization, EmailAddress, Group):
        # If something other than enter is inputed, it becomes the new ex: FirstName.
        if (not FirstName == ''):
            self.FirstName = FirstName 
        if (not LastName == ''):
            self.LastName = LastName
        if (not PhoneNumber == ''):
            self.PhoneNumber = PhoneNumber
        if (not Address == ''):
            self.Address == Address
        if (not Organization == ''):
            self.Organization = Organization
        if (not EmailAddress == ''):
            self.EmailAddress = EmailAddress
        if (not Group == ''):
            self.Group = Group

     
        

