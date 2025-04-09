# write a program to create a class with attribute 'name', 'account' and 'balance' and functionalities
# like change pin, deposit, withdraw, check balance and transfer money.

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
                new_pin = int(input("Enter new pin: "))
                self.change_pin(new_pin)
             elif self.choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
             elif self.choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
             elif self.choice == 4:
                self.check_balance()
             elif self.choice == 5:
                amount = float(input("Enter the amount to transfer: "))
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

    
    def change_pin(self, new_pin):
        if isinstance(new_pin, int) and len(str(new_pin)) == 4:
            self.pin = new_pin
            print("Pin changed successfully.")
        else:
            print("Invalid pin. Please enter a 4-digit number.")
        

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
        else:
            print("Invalid amount. Please enter a valid amount.") 
        

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a valid amount.")
        

    def check_balance(self):
        print("Your current balance is: ", self.balance)
        

    def transfer_money(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Money transferred successfully.")
            else:
                print("Insufficient balance.")
        

    def exit(self):
        print("Thank you for using the Bank Account Management System. Goodbye!")
        
    
    

user1 = BankAccount("Akshit Thakur", "2311083")
