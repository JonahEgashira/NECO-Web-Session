class Bank:

    balance = 0
    destination_balance = 0
    change_amount = 0

    def __init__(self, balance, destination_balance):
        self.balance = balance
        self.destination_balance = destination_balance

    def withdraw(self, change_amount):
        self.balance -= change_amount
        print("My balance left: " + str(self.balance))
        
    def deposit(self, change_amount):
        self.balance += change_amount
        print("My balance left: " + str(self.balance))

    def send_money(self, change_amount):
        self.balance -= change_amount
        self.destination_balance += change_amount
        print("My balance left: " + str(self.balance))
        print("Destination balance left: " + str(self.destination_balance))


Mybank = Bank(100, 100)
Mybank.withdraw(100)
Mybank.deposit(5000)
Mybank.send_money(300)



