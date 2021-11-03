class BankAccount:
    bank_name = "Bank of Hyrule"
    account = []
    def __init__(self, int_rate = .025, balance= 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    def display_account_info(self):
        print (f"Balance:${self.balance}")
        return self

class User:
    population = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .025, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    def user_yield_interest(self):
        self.account.yield_interest()
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self


bankAccount_A = BankAccount()
bankAccount_B = BankAccount()

chris = User("Chris", "cbonz@gmail.com")
chris.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(1000).user_yield_interest()

#bankAccount_A.deposit(100).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()
#bankAccount_B.deposit(1000).deposit(2000).withdraw(1000).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

#print(bankAccount_A.display_account_info)
#print(bankAccount_B.display_account_info)

chris.display_user_balance()