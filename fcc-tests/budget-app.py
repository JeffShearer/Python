# replit https://replit.com/@JeffShearer/boilerplate-budget-app


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
        self.withdrawals = float()
    
    
    #Built in method for determining what happens with the object itself is printed
    def __str__(self):
        #variable to create 30 char string with name & asterisks
        title = self.name.center(30,'*')
        body = ""
        #total calls the get_balance method and rounds to two decimal places
        total = "Total: " + str(round(self.get_balance(),2))
        # For loop that iterates through the range of self.ledger, grabbing the first 23 chars of description and first 7 of amount   
        for item in range(len(self.ledger)):
            body += self.ledger[item]['description'][0:23]+ str(self.ledger[item]['amount'])[0:7].rjust(30-len(self.ledger[item]['description'][0:23])) + '\n'
        return title + '\n' + body + total

 
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
            # sum all withdrawals to be used later for the spend chart method
            self.withdrawals += amount
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
            # sum all withdrawals to be used later for the spend chart method
            self.withdrawals += amount         
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
    
# separate method to return a chart of categories and the percentage spent. This works fine in my testing 
def create_spend_chart(categories):
    output = ""
    labels = ""
    cat_list = []
    percent_list= []
    arg_count = len(categories)
    

    for cat in categories:
        # generate lists for category names and percentages
        cat_list.append(cat.name)
        # Calculate the percentage spent based on withdrawals / initial deposit
        percent_list.append(round(100*(cat.withdrawals / cat.ledger[0]['amount']),-1))
        row = ""
        # Creates y-axis labels and values, across a range of 0-100 inclusive
        for val in reversed(range(0,110,10)):
            string = str(val).rjust(3) + "|"

            # compare percentage values to the y-axis and populate bar chart accordingly
            for x in percent_list:
                if x >= val:
                    string += " o "
                else:
                    string += "  "
            string = string.rstrip()
            # iterate a new row for each percentile
            row += string + "\n"

    #Determine longest category name, then add trailing spaces to shorter categories so all have same len
    long_cat_name = len(max(cat_list,key=len))
    for name in range(len(cat_list)):
        if len(cat_list[name]) != long_cat_name:
            cat_list[name] = cat_list[name] + ' '*(long_cat_name-len(cat_list[name]))
        else:
            cat_list[name] = cat_list[name]

#Creates dash line based on quantity of arguments supplied
    dashes = '    '
    dashes += '-'*(1+3*arg_count)

#Prints labels vertically
    for value in range(0,long_cat_name):
        labels += '     '
        number = 1
        for name in cat_list:
            if number == 1:
                labels += (name[value] + ' ')
                number += 1
            else: 
                labels += (' ' + name[value] + ' ')
                number += 1
        labels += '\n'
    labels = labels.rstrip()
    labels += "  "


   
    output = 'Percentage spent by category' + '\n' + row + '\n' + dashes + '\n' + labels
    return  output


food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.withdraw(10)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(500, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
test = Category("test")
test.deposit(1000)
print(create_spend_chart([food, clothing, auto,test]))
print(food)