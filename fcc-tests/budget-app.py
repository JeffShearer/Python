# replit https://replit.com/@JeffShearer/boilerplate-budget-app
# instructions https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

class Category:
    ledger = []
    name = ""
    total = float()

    # initialize new budget category objects -
    # note you need to define as variables anything you plan to reference in other methods!
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.total = float()

    # Method for deposit w/ two arguments - amount & descripption - append to a ledger (dictionary)
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount,'description': description})
        # increment the total by the added amount for get_balance inquiries
        self.total += float(amount)


     #Withdraw method - same as deposit but passes negative fund.
    def withdraw(self,amount,description=""):
        # uses check_funds method to confirm if enough total remains in categroy to perform withdrawal
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -amount,'description': description})
            #decrement the total and set withdraw to True to allow return statement to validate
            self.total -= amount
            return True
        else:
            return False
 

    #get balance method - returns current balance in the ledger.
    def get_balance(self):
        return self.total

    #transfer method that takes an amount and moves from one category to another
    def transfer(self,amount,newcat):
        # similar to withdraw - uses check_funds method to determine if transfer can be processed
        if self.check_funds(amount) is True:
            transferto_desc = str("Transfer to " + newcat.name)
            transferfrom_desc= str("Transfer from " + self.name)
            self.ledger.append({'amount': -amount,'description': transferto_desc})
            #decrement the total and set withdraw to True to allow return statement to validate
            self.total -= amount          
            description = newcat
            newcat.deposit(amount,transferfrom_desc)
            return True
        else:
            return False
        
    # Check funds - checks amount in category for use with withdraw & transfer methods
    def check_funds(self,amount):
        if self.total >= amount:
            return True
        else:
            return False



def create_spend_chart(categories):
    return

food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.withdraw(10)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(500, clothing)
print(food.ledger)
print(clothing.ledger)
print(clothing.get_balance())
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

