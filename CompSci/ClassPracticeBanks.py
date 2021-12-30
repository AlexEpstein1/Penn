class BankAccount(object):
	
	#constructor
	def __init__(self, owner):
		#define your instance variables here
		self.owner = owner
		self.balance = 0 #default value of 0 banl balance

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	#stringify the object
	def __str__(self):
		return "Account owned by " + self.owner + " has balance = " + str(self.balance) 

	def transfer(self, other_account, amount):
		 #sel.balance -= amount
		 self.withdraw(amount)
		 other_account.deposit(amount)

		#transfer money from this account to some other account



def main():
	account1 = BankAccount("alex")
	account1.deposit(1000)
	account1.withdraw(50)
	
	account2 = account1
	account2.withdraw(50)
	print(account1)

	account3 = BankAccount("abcd")
	account1.transfer(account3,50)
	print(account1)

main()