class Details:
    def __init__(self, name, account_number, amount=100):
        self.name = name
        self.account_number = account_number
        self.amount = amount

    def deposit(self, taka):
        if taka > 0:
            self.amount += taka

    def withdraw(self, amount):
        if amount > 0 and amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient balance or invalid amount!")

    def transfer(self, target_account, taka):
        if taka > 0 and taka <= self.amount:
            self.amount -= taka
            target_account.amount += taka
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print(f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.amount}")


# User inputs for creating the first person
name1 = input("Enter the name of the first account holder: ")
account_number1 = int(input("Enter the account number for the first account: "))
initial_amount1 = float(input("Enter the initial amount for the first account: "))

# User inputs for creating the second person
name2 = input("Enter the name of the second account holder: ")
account_number2 = int(input("Enter the account number for the second account: "))
initial_amount2 = float(input("Enter the initial amount for the second account: "))

# Creating instances of Details using user inputs
person1 = Details(name1, account_number1, initial_amount1)
person2 = Details(name2, account_number2, initial_amount2)

# Display initial balances
person1.display()
print('\n')
person2.display()
print('\n')

# Deposit money into person1's account
deposit_amount = float(input(f"Enter amount to deposit into {name1}'s account: "))
person1.deposit(deposit_amount)
person1.display()
print('\n')

# Withdraw money from person1's account
withdraw_amount = float(input(f"Enter amount to withdraw from {name1}'s account: "))
person1.withdraw(withdraw_amount)
person1.display()
print('\n')

# # Transfer money from person1 to person2
# transfer_amount = float(input(f"Enter amount to transfer from {name1}'s account to {name2}'s account: "))
# person1.transfer(person2, transfer_amount)
# person1.display()
# person2.display()

print('\n')
transfer_amount = float(input(f"Enter amount to transfer from {name2}'s account to {name1}'s account: "))
person2.transfer(person1, transfer_amount)
person1.display()
person2.display()
