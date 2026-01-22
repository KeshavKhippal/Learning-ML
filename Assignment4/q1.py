class BankAccount:
    def __init__(self,num,name,balance):
        self.accountNumber=num
        self.owner_name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited sucessfully")
    def withdraw(self,amount):
        self.balance-=amount
        print("Amoutn withdrawn successfully")
    def checkBalance(self):
        print("Current Account Balance is ",self.balance)
