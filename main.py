



#-------------------->>>>>     MENU  --  MAKER     <<<<<--------------------

def menuLoad(menu):

    count = 1

    for z in menu:

        print(f"{count}. {z}")

        count += 1

    print(f"0. EXIT")

    selection = input("\nEnter Number: ")



    if selection.isnumeric():

        selection = int(selection)

        if selection not in range(0, count):

            print("\nError: Number outside range\n")

            selection = 99

    else:

        print("\nError: Input must be a Number\n")

        selection = 99



    return selection



#-------------------->>>>>      FIND Customer      <<<<<--------------------

def custFind():

    found = 0

    print("---------- FIND Customer ----------")

    findMenu = ["by NAME", "by NUMBER"]

    selection = menuLoad(findMenu)



    if selection == 1:

        findFName = input("Enter FIRST Name: ").lower()

        findLName = input("Enter LAST Name : ").lower()



        for x in custList:

            if x.CustFName.lower() == findFName and x.CustLName.lower() == findLName:

                found = x

                print("Customer FOUND")

                break



    elif selection == 2:

        findNum = input("Enter Account Number: ")



        if findNum.isnumeric():

            findNum = int(findNum)



            for y in custList:

                if y.CustAcct.AccNum == findNum:

                    found = y

                    print("Customer FOUND")

                    break

        else:

            print("Error")



    return found


#-------------------->>>>>      ADD  Customer      <<<<<--------------------

def custAdd():

    newFName = input("Enter FIRST Name: ")

    newLName = input("Enter LAST Name:  ")

    pickType = int(input("1. Savings\n" 

                       "2. Cheque\n" 

                       "3. Business: "))



    if pickType == 3:

        newAccType = "Business"

    elif pickType == 2:

        newAccType = "Cheque"

    else:

        newAccType = "Savings"



    newCust = Customer(Account(newAccType), newFName, newLName)

    custList.append(newCust)

    print("New Customer ADDED")

    print(custList[len(custList)-1])



#-------------------->>>>>      EDIT Customer      <<<<<--------------------

def custEdit():

    fileEdit = custFind()



    if fileEdit != 0:

        editMenu = ["FIRST Name", "LAST Name", "EMAIL", "Account TYPE"]

        editPick = menuLoad(editMenu)



        if editPick == 1:

            fileEdit.setFName()

        elif editPick == 2:

            fileEdit.setLName()

        elif editPick == 3:

            fileEdit.setEmail()

        elif editPick == 4:

            fileEdit.CustAcct.setType()

        else:

            print("Error")



#-------------------->>>>>      MAIN  PROGRAM      <<<<<--------------------

from Accounts import Account

from Customers import Customer



custList = []


dat01 = Customer(Account("Savings"), "Kylie", "Mackay")

dat02 = Customer(Account("Cheque"), "Donna", "Underwood")

dat03 = Customer(Account("Business"), "Anthony", "Hudson")



custList.extend([dat01, dat02, dat03])


menu1 = ["DEPOSIT", "WITHDRAW", "Customer Menu"]

menu2 = ["FIND", "ADD", "EDIT", "Show ALL"]



while True:

    choice1 = menuLoad(menu1)


    if choice1 == 0:

        print("Goodbye")

        break



    elif choice1 == 1:

        depFind = custFind()



        if depFind != 0:

            print(f"Current Balance: {depFind.CustAcct.getBal()}")

            depAmt = input("Enter DEPOSIT Amount: ")

            if depAmt.isnumeric():

                depAmt = float(depAmt)

                depFind.Deposit(depAmt)



    elif choice1 == 2:

        print("Withdraw function here!!!")



    elif choice1 == 3:



        choice2 = menuLoad(menu2)



        if choice2 == 1:

            found = custFind()
