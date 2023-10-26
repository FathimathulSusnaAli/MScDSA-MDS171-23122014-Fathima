
class BankAccount():
    def __init__(self,Name):
        self.name = Name
        
    def deposit(self,deposit):
        self.Deposit = deposit
        total = 0
        for i in balance:
            if balance[i]>=0:
                if i ==self.name:
                    total += balance[i]+self.Deposit
                    print(total)
                    balance[self.name]=total
        print(total)
    def withdraw(self,withdraw):
        total = 0
        self.Withdraw = withdraw
        for i in balance:
            if balance[i]>=0:
                if i ==self.name:
                    total = balance[i]-withdraw
                    print(total)
                    balance[self.name]=total
            print(total)

    def viewdetails(self):
        print(self.name,balance[self.name])



# amount = int(input("Enter the Amount"))
# account.deposit(amount)
# withdraw = int(input("Amount to withdrawn"))
# account.withdraw(withdraw)
# inputoption = int(input("Enter the Input"))

balance = {"Ram":5000,"Priya":400}

Name = input("Enter the Name: ")
account = BankAccount(Name)

if Name in balance:
    while True:
        user_input = int(input("Enter the Input (1/2)"))
        print("1. To Deposit")
        print("2. To Withdraw")
        if user_input == 1:
            user_deposit = int(input("Enter the Input"))
            account.deposit(user_deposit)
        elif user_input == 2:
            user_withdraw = int(input("Enter the amount to Withdraw"))
            account.withdraw(user_withdraw)
        elif user_input == 3:
            account.viewdetails()

        elif user_input == 4:
            exit()


else:
    print("Incorrect Entry")
    exit()
    




