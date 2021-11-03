class BankAccount:
    bank_name = "Bank of Hyrule"
    account = []
    def __init__(self, int_rate = .025, balance= 0):
        self.int_rate = int_rate
        self.balance = balance
        self.interest = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        self.interest = self.balance*self.int_rate
        return self
    def display_account_info(self):
        self.display_account_info = (f"Balance:${self.balance + self.interest}")
        return self

class User:
    population = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .025, balance = 0)
    def make_deposit(self):
        self.account.deposit()
    def make_withdrawal(self):
        self.account.withdraw()
    def display_user_balance(self):
        self.account.display_account_info()
    


bankAccount_A = BankAccount()
bankAccount_B = BankAccount()

chris = User("Chris", "cbonz@gmail.com")
chris.make_deposit(1000)

bankAccount_A.deposit(100).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()
bankAccount_B.deposit(1000).deposit(2000).withdraw(1000).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

print(bankAccount_A.display_account_info)
print(bankAccount_B.display_account_info)

print(chris.display_user_balance)
