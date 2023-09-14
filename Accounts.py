class Account():

    count = 100000


    def __init__(self, newType):

        Account.count += 1000

        self.AccNum = Account.count

        self.AccType = newType

        self.AccBal = 0.00


    def getNum(self):

        return self.AccNum


    def getType(self):

        return self.AccType


    def setType(self):

        print(f"Current Account Type: {self.AccType}")

        print("SAVINGS", "CHEQUE", "BUSINESS")

        newType = input("Enter New Account TYPE: ")

        self.AccType = newType


    def getBal(self):

        return self.AccBal
