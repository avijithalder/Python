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
            self.amount = self.amount - amount
        else:
            print("Insufficient balance or invalid amount!")

    def transfer(self, target_account, taka):
        if taka > 0 and taka <= self.amount:
            self.amount = self.amount - taka
            target_account.amount = target_account.amount + taka
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print(f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.amount}")


# Creating instances of Details
person1 = Details('Avijit', 101, 1500)
person2 = Details('Mondira', 105, 3000)

# Display initial balances
person1.display()
person2.display()
print('\n')

# Deposit money into person1's account
person1.deposit(500)
person1.display()
print('\n')

# Withdraw money from person1's account
person1.withdraw(800)
person1.display()
print('\n')

# Transfer money from person1 to person2
person1.transfer(person2, 300)
person1.display()
person2.display()
