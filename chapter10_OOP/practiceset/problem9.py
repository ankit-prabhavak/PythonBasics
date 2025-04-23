# write a program to create a class with attribute 'name', 'account' and 'balance' and functionalities
# like change pin, deposit, withdraw, check balance and transfer money.
import time

class BankAccount:
    # Attributes
    name = "John Doe"
    account = "123456789"
    balance = 0
    pin = 1234

    choice = 0

    def __init__(self, name, account):
        self.name = name
        self.account = account
        print("Welcome to the Bank Account Management System")
        print(f"User: {self.name}       Account Number: {self.account}")
        print("Please create your PIN to proceed\n")
        self.create_pin()
        print("1. Change Pin")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")
        self.choice = int(input("Enter your choice: "))
        
        log = "yes"
        while(log == "yes"):
             
             if self.choice == 1:
                self.verifier()
                new_pin = int(input("Enter new pin: "))
                self.change_pin(new_pin)
             elif self.choice == 2:
                amount = float(input("Enter the amount to deposit: \u20B9"))
                self.verifier()
                self.deposit(amount)
             elif self.choice == 3:
                amount = float(input("Enter the amount to withdraw: \u20B9"))
                self.verifier()
                self.withdraw(amount)
             elif self.choice == 4:
                self.verifier()
                self.check_balance()
             elif self.choice == 5:
                amount = float(input("Enter the amount to transfer: \u20B9"))
                self.verifier()
                self.transfer_money(amount)
             elif self.choice == 6:
                self.exit()
                break
             else:
                print("Invalid choice. Please try again.")
                self.__init__(self.name, self.account)

             log = input("Do you want to continue? (yes/no): ")
             if log == "yes":
                self.choice = int(input("Enter your choice: "))
             else:
                print("Thank you for using the Bank Account Management System. Goodbye!")
                break

    
    def create_pin(self):
        temp = int(input("Enter your PIN: "))
        confirm_pin = int(input("Confirm PIN: "))

        if temp == confirm_pin:
            self.pin = temp
            self.processing()
            print("PIN created successfully.")
        else:
            print("PINs do not match. Please try again.")
            self.create_pin()

       
      

    def change_pin(self, new_pin):
        if isinstance(new_pin, int) and len(str(new_pin)) == 4:
            self.pin = new_pin
            print("Pin changed successfully.")
        else:
            print("Invalid pin. Please enter a 4-digit number.")
        

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            print("Amount deposited successfully. Current balance: \u20B9", self.balance)
        else:
            print("Invalid amount. Please enter a valid amount.") 
        

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully. Current balance: \u20B9", self.balance)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a valid amount.")
        

    def check_balance(self):
        print("Your current balance is: \u20B9", self.balance)
        

    def transfer_money(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Money transferred successfully. Current balance: \u20B9", self.balance )
            else:
                print("Insufficient balance.")
    
    def verifier(self):
        print("Verify your identity")
        entry = input("PIN: ")
        if entry == str(self.pin):
            print("Verification successful.")
            self.processing()
        else:
            print("Verification failed. Please try again.")
            self.verifier()


    def exit(self):
        print("Thank you for using the Bank Account Management System. Goodbye!")

    def processing(self):
        time.sleep(1)
        print("Processing your request...")
        time.sleep(1)
       
        
    
    

user1 = BankAccount("Ankit Kumar", "2311601")
