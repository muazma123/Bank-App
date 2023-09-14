class Customer():

    emailSuffix = "@MyBank.co.nz"



    def __init__(self, newAcct, newFName, newLName):

        self.CustAcct = newAcct

        self.CustFName = newFName

        self.CustLName = newLName

        self.CustEmail = newFName + "." + newLName + Customer.emailSuffix


    def setFName(self):

        newF = input("Enter New FIRST Name: ")

        self.CustFName = newF



    def setLName(self):

        newL = input("Enter New LAST Name: ")

        self.CustLName = newL


    def setEmail(self):

        newEmail = input("Enter New EMAIL: ")

        self.CustEmail = newEmail


    def Deposit(self, depAmt):

        self.CustAcct.AccBal += depAmt


    def Withdraw(self, wdrAmt):

        self.CustAcct.AccBal -= wdrAmt


    def __str__(self):

        return (f"Account Number : {self.CustAcct.AccNum}\n" 

                f"Account Name   : {self.CustFName} {self.CustLName}\n" 

                f"Account Email  : {self.CustEmail}\n" 

                f"Account Type   : {self.CustAcct.AccType}\n" 

                f"Account Balance: {self.CustAcct.AccBal}\n")
