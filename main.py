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


    #check do acc already exits
    def isExists(self,acc_no):
        for acc in self.accounts:
            if acc.acc_no==acc_no:
                return True

        return False

    #create acc
    def create_account(self):
        acc_type=input("Savings or Current:")
        acc=None
        acc_no=int(input("Enter Account Number:"))
        holder_name=input("Enter Holder Name:")

        if acc_type=="Savings" and self.isExists(acc_no):
            acc=SavingAccount(acc_no,holder_name,500)
        else:
            acc=CurretAccount(acc_no,holder_name,500)

        self.accounts.append(acc)
        print("account created successfully")
        print("\n")

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
        print("\n")

    #withdraw
    def withdraw_amount(self):
        acc_no=int(input("Enter Account Number:"))
        traget_acc=None
        for acc in self.accounts:
            if acc.acc_no==acc_no:
                traget_acc=acc
                break

        if not traget_acc:
            print("Account Not Found")
            return
        amount=int(input("Enter Amount:"))
        traget_acc.withdraw(amount)
        print("\n")

    #transfer
    def send_amount(self):
        sender=int(input("enter your account no. :"))
        target_sender=None

        for acc in self.accounts:
            if acc.acc_no==sender:
                target_sender=acc
                break

        if not target_sender:
            print("your Account Not Found")
            return

        reciver=int(input("enter receiver account no. :"))
        targer_receiver=None

        for acc in self.accounts:
            if acc.acc_no==reciver:
                targer_receiver=acc
                break

        if not targer_receiver:
            print("Receivers Account Not Found")
            return

        amount=int(input("Enter Amount:"))
        target_sender.withdraw(amount)
        targer_receiver.deposit(amount)

        print(f"succfully transfered {amount} to {target_sender.holder_name} ")
        print("\n")


    #delete acc
    def remove_account(self):
        acc_no=int(input("Enter Account Number:"))
        traget_acc=None
        for acc in self.accounts:
            if acc.acc_no==acc_no:
                targer_acc=acc
                break
        if not targer_acc:
            print("Account Not Found")
            return

        self.accounts.remove(traget_acc)
        print("account removed successfully")

    #display_all acc
    def all_acc(self):
        print("Account list:")
        print("Acc no \t Name \t Balance")
        for acc in self.accounts:
            print(acc.acc_no ,"\t",acc.holder_name,"\t",acc.balance)


def main():
    hdfc=Bank()
    hdfc.create_account()
    hdfc.create_account()
    hdfc.all_acc()

if __name__ == "__main__":
    main()
