# replit https://replit.com/@JeffShearer/boilerplate-budget-app
# instructions https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

class Category:
    ledger = []
    name = ""
    # initialize new budget category objects -
    # note you need to define name and ledger, and anythign else that's object-instance specific
    # for other methods to work properly!
    def __init__(self,name):
        self.name = name
        self.ledger = []
        print(self.name, "constructed")

    # Method for deposit w/ two arguments - amount & descripption - append to a ledger (dictionary)
    def deposit(self, amount, description=""):
        self.ledger.append({'Amount': amount,'Description': description})

     #Withdraw method - same as deposit but passes negative fund.
    def withdraw(self,amount,description=""):
        self.ledger.append({'Amount': -amount,'Description': description})
        return print("True")

    #get balance method - returns current balance in the ledger showing all deposits & withdrawals
    def get_balance(self):
        print(self.name, self.ledger)

e = Category('Entertainment')
f = Category('Food')
e.deposit(100,"movies")
f.deposit(50,'Groceries')
e.withdraw(100, 'Gas')
f.get_balance()
e.get_balance()

    #transfer method - move funds from one ledger item to another

    # check funds 
#Besides the Category class, create a function (outside of the class) called 
# create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.
#def create_spend_chart(categories):
    #return


#Basic tests

#food = budget.Category("Food")
#food.deposit(1000, "initial deposit")
#food.withdraw(10.15, "groceries")
#food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
#clothing = budget.Category("Clothing")
#food.transfer(50, clothing)
#clothing.withdraw(25.55)
#clothing.withdraw(100)
#auto = budget.Category("Auto")
#auto.deposit(1000, "initial deposit")
#auto.withdraw(15)

#print(food)
#print(clothing)

# print(create_spend_chart([food, clothing, auto]))
