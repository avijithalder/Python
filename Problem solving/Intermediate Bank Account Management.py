class AccountDetails:
    print("Avijit Bank LTD.")

    def __init__(self, name, account_number, amount, password):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.password = password
        self.authenticated = False

    def authenticate(self):
        if not self.authenticated:
            input_password = input("Enter Your Password")
            if input_password == self.password:
                self.authenticated = True
                print("Authentication successful!")
                return True
            else:
                print("Incorrect Password! ")
                return False
        return True

    def display(self):
        if self.authenticate():
            print('Account Name:', self.name)
            print('Account Number:', self.account_number)
            print('Balance:', self.amount)

    def deposit(self, balance):
        if self.authenticate():
            if balance > 0:
                self.amount = self.amount + balance
                print(f"₹{balance} deposited. New Balance: ₹{self.amount}")
            else:
                print("Deposit amount must be positive!")

    def withdraw(self, balance):
        if self.authenticate():
            if balance > 0 and balance <= self.amount:
                self.amount = self.amount - balance
                print(f"₹{balance} withdrawn. New Balance: ₹{self.amount}")
            else:
                print("Invalid withdrawal amount or insufficient balance!")

    def transfer(self, balance, receiver_account):
        if self.authenticate():
            if balance > 0 and balance <= self.amount:
                self.amount = self.amount - balance
                print(f"₹{balance} transferred to Account: {receiver_account}. New Balance: ₹{self.amount}")
            else:
                print("Invalid transfer amount or insufficient balance!")


person1 = AccountDetails('Avijit', 101, 500, '123')
person2 = AccountDetails('Mondira', 102, 100, '456')

while True:
    account_choice = int(input("Enter Your Account Number: "))
    if account_choice == 101:
        selected_account = person1
    elif account_choice == 102:
        selected_account = person2
    else:
        print("invalid choice,Please Try Again.")
        continue

    print("\nChoose an option:")
    print("0.Account Details")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("9. Back")
    print("4. Exit")
    press = int(input("Enter your choice: "))

    if press == 0:
        selected_account.display()
    elif press == 1:
        amount = float(input("Enter the deposit amount: "))
        selected_account.deposit(amount)
        selected_account.display()
    elif press == 2:
        amount = float(input("Enter the withdrawal amount: "))
        selected_account.withdraw(amount)
        selected_account.display()
    elif press == 3:
        amount = float(input("Enter the transfer amount: "))
        receiver_account = int(input("Enter the receiver's account number: "))
        selected_account.transfer(amount, receiver_account)
        selected_account.display()
    elif press == 9:
        b = account_choice
        print(b)
    elif press == 4:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
