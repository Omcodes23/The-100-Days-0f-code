class Bank:
    def __init__(self,accnumber,name,balance):
        self.acno = accnumber
        self.name = name
        self.bal = balance 
        print("Welcome to the banking application using python")
    
    def deposit(self,amo):
        self.bal += amo 
        print("The amount is Deposited")
        print(f"The new amount is : {self.bal}")

    def withdraw(self,amo):
        if amo > self.bal:
            print("impossible operation you didn't have sufficient amount")
        else:
            self.bal -= amo

    def display(self):
        print(f"The current amount is : {self.bal}")
        print(f"The account number is : {self.acno}")
        print(f"The account balance is : {self.bal}")

if __name__ == "__main__":
    accno = int(input("enter your 10 digit acc number : "))
    name = input("Enter your name : ")
    bal = int(input("Enter your balance : "))
    op = Bank(accno,name,bal)
    print("<--> Choose your operation number <-->")
    print()
    while True:
        print("*"*30)
        choice = int(input("\n 1 - Deposit amount \n 2 - Withdraw amount \n 3 - display details \n 4 - exit \n -->> "))
        print("*"*30)
        if choice == 1 :
            amo = int(input("Enter the amount to deposit : "))
            op.deposit(amo)
        elif choice == 2 :
            amo = int(input("Enter the Amount to Withdraw : "))
            op.withdraw(amo)
        elif choice == 3:
            op.display()
        elif choice == 4:
            print("Thank you for visiting")
            print("Bye 🤞✌🤞")
            break
        else : 
            print("please enter the valid choice")
