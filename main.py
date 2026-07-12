from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,acc_no,holder_name,balance):
        self.acc_no=acc_no
        self.holder_name=holder_name
        self.balance=balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    def display_balance(self):
        print("Account Number:", self.acc_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)

    def deposit(self,amount):
        self.balance += amount
        self.display_balance()

class SavingAccount(Account):
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            self.display_balance()
            print(f"withdraw {amount}")
        else:
            self.display_balance()
            print("You don't have enough money to withdraw")

class CurretAccount(Account):
    def withdraw(self,amount):
        if amount < self.balance+5000:
            self.balance -= amount
            self.display_balance()
            print(f"withdraw {amount}")
        else:
            self.display_balance()
            print("You don't have enough money to withdraw")

class Bank():
    def __init__(self):
        self.accounts=[]

    #create acc
    def create_account(self):
        acc_type=input("Savings or Current:")
        acc=None
        acc_no=int(input("Enter Account Number:"))
        holder_name=input("Enter Holder Name:")

        if acc_type=="Savings":
            acc=SavingAccount(acc_no,holder_name,500)
        else:
            acc=CurretAccount(acc_no,holder_name,500)

        self.accounts.append(acc)
        print("account created successfully")
        acc.display_balance()

    #deposit
    def deposit_amount(self):
        acc_no=int(input("Enter Account Number:"))

        target_acc=None
        for acc in self.accounts:
            if acc.acc_no==acc_no:
                target_acc=acc
                break

        if not target_acc:
            print("Account Not Found")
            return
        amount=int(input("Enter Amount:"))
        target_acc.deposit(amount)
        target_acc.display_balance()



    #withdraw

    #transfer

    #delete acc

    #display_all acc


def main():
    hdfc=Bank()
    hdfc.create_account()
    hdfc.deposit_amount()

if __name__ == "__main__":
    main()
