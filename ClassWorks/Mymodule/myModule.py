class student:
    def __init__(self,Name,PhoneNumber) :          #initialize the data members to the instance of the class.
        self.name = Name
        self.phonenumber = PhoneNumber
    
    def printStudent(self):
        print("The Name is {} with the phone number {}".format(self.name,self.phonenumber))





    