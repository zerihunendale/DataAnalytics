class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to hold account information
        self.transactions = []  # List to hold transaction history

    def create_account(self, name, initial_balance):
        if name in self.accounts:
            print(f"Account for {name} already exists.")
            return
        self.accounts[name] = {
            'balance': initial_balance,
            'transactions': []  # List to hold individual transactions for the account
        }
        self.transactions.append((name, 'Account Created', initial_balance))
        print(f"Account created for {name} with initial balance ${initial_balance:.2f}.")

    def deposit(self, name, amount):
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.accounts[name]['balance'] += amount
        self.accounts[name]['transactions'].append((amount, 'Deposit'))
        self.transactions.append((name, 'Deposit', amount))
        print(f"${amount:.2f} deposited to {name}'s account. New balance: ${self.accounts[name]['balance']:.2f}.")

    def withdraw(self, name, amount):
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.accounts[name]['balance']:
            print("Insufficient funds.")
            return
        self.accounts[name]['balance'] -= amount
        self.accounts[name]['transactions'].append((-amount, 'Withdrawal'))
        self.transactions.append((name, 'Withdrawal', amount))
        print(f"${amount:.2f} withdrawn from {name}'s account. New balance: ${self.accounts[name]['balance']:.2f}.")

    def view_balance(self, name):
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return
        balance = self.accounts[name]['balance']
        print(f"{name}'s account balance: ${balance:.2f}.")

    def print_transactions(self, name):
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return
        transactions = self.accounts[name]['transactions']
        print(f"Transaction history for {name}:")
        for amount, trans_type in transactions:
            print(f"{trans_type}: ${abs(amount):.2f}")

    def print_all_transactions(self):
        print("All Transactions:")
        for trans in self.transactions:
            print(f"{trans[0]} - {trans[1]}: ${trans[2]:.2f}")


# Example usage
bank = Bank()
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

bank.deposit("Alice", 200)
bank.withdraw("Bob", 100)
bank.view_balance("Alice")
bank.print_transactions("Alice")
bank.print_all_transactions()