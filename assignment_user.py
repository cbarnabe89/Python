class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.display = (f"User:{self.name}, Balance:{self.account_balance}")
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received
    def display_user_balance(self):
        self.display = (f"User:{self.name}, Balance:${self.account_balance}")
        

guido = User("Guido","guido@gmail.com")
monty = User("Monty", "monty@gmail.com")
barnabe = User("Barnabe", "cbonz@gmail.com")

barnabe.make_deposit(10000)
barnabe.make_deposit(10000)
barnabe.make_deposit(10000)
barnabe.make_withdrawal(5000)
guido.make_deposit(500)
guido.make_deposit(500)
guido.make_withdrawal(50)
guido.make_withdrawal(50)
monty.make_deposit(1000)
monty.make_withdrawal(100)
monty.make_withdrawal(100)
monty.make_withdrawal(100)
guido.display_user_balance()
monty.display_user_balance()
barnabe.display_user_balance()

print(guido.account_balance)
print(monty.account_balance)
print(barnabe.account_balance)
print(guido.display)
print(monty.display)
print(barnabe.display)