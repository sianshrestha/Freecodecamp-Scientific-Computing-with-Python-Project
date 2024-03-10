class Category:
  
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.funds = 0
      
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount
      
    def withdraw(self, amount, description=""):
        if self.funds - amount >= 0:
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            return True
        else:
            return False
          
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
      
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
             return False
          
    def check_funds(self, amount):
        return self.funds - amount >= 0

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        result = title + items + f"Total: {total:.2f}"
        return result


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    total_spent = 0
    category_spent = {}

    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        total_spent += spent
        category_spent[category.category] = spent
    
    for category in categories:
        category_spent[category.category] = int(category_spent[category.category] / total_spent * 100)
    
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for category in categories:
            if category_spent[category.category] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_length = max(len(category.category) for category in categories) 
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
    
    return chart

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")    
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55,"groceries")
entertainment.withdraw(33.40,"movies")
business.withdraw(10.99,"invest")

print(food)

print(create_spend_chart([business, food, entertainment]))