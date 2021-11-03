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


bankAccount_A = BankAccount()
bankAccount_B = BankAccount()

bankAccount_A.deposit(100).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()
bankAccount_B.deposit(1000).deposit(2000).withdraw(1000).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

print(bankAccount_A.display_account_info)
print(bankAccount_B.display_account_info)


