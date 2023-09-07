class BankSystem:
    def __init__(self):
        self.balance = 0
        self.password = "1234"  # Default password
    
    def cash_withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        else:
            print("Invalid amount or insufficient balance.")
    
    def cash_credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount credited. Updated balance: {self.balance}")
        else:
            print("Invalid amount.")
    
    def change_password(self, new_password):
        if len(new_password) >= 4:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Password should be at least 4 characters long.")
    
    def display_balance(self):
        print(f"Current balance: {self.balance}")
    
    def menu(self):
        while True:
            print("Welcome to the Bank System!")
            print("1. Cash Withdrawal")
            print("2. Cash Credit")
            print("3. Change Password")
            print("4. Display Balance")
            print("5. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                amount = float(input("Enter amount to withdraw: "))
                self.cash_withdraw(amount)
            elif choice == 2:
                amount = float(input("Enter amount to credit: "))
                self.cash_credit(amount)
            elif choice == 3:
                new_password = input("Enter new password: ")
                self.change_password(new_password)
            elif choice == 4:
                self.display_balance()
            elif choice == 5:
                print("Thank you for using the Bank System!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Create an instance of BankSystem
bank = BankSystem()

# Display the menu and process user input
bank.menu()
