class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.display = (f"User:{self.name}, Balance:{self.account_balance}")
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received
        return self
    def display_user_balance(self):
        self.display = (f"User:{self.name}, Balance:${self.account_balance}")
        return self
        

guido = User("Guido","guido@gmail.com")
monty = User("Monty", "monty@gmail.com")
barnabe = User("Barnabe", "cbonz@gmail.com")

barnabe.make_deposit(10000).make_deposit(10000).make_deposit(10000).make_withdrawal(5000).display_user_balance()
guido.make_deposit(500).make_deposit(500).make_withdrawal(50).make_withdrawal(50).display_user_balance()
monty.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()


print(guido.account_balance)
print(monty.account_balance)
print(barnabe.account_balance)
print(guido.display)
print(monty.display)
print(barnabe.display)