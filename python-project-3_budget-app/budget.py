import math

class Category:
  
  def __init__(self, name):
    print(" ")
    self.name = name
    self.ledger = []
    self.funds = 0
    self.spent = 0

  def deposit(self, amount, description = ""):
    self.funds = self.funds + amount
    self.ledger.append({"amount" : amount, "description" : description})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.funds = self.funds - amount
      self.spent = self.spent + amount
      self.ledger.append({"amount" : -amount, "description" : description})
      return True
    else:
      return False

  def get_balance(self):
    return self.funds

  def transfer(self, amount, Category):
    if self.check_funds(amount):
      self.funds = self.funds - amount
      self.spent = self.spent + amount
      self.ledger.append({"amount" : -amount, "description" : "Transfer to "+Category.name})
      Category.funds = Category.funds + amount
      Category.ledger.append({"amount" : amount, "description" : "Transfer from "+self.name})
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.funds >= amount:
      return True
    else:
      return False

  def __str__(self):
    self.character_length = len(self.name)
    self.star_length = int(0.5*(30 - self.character_length))
    
    self.title = ("*"*(self.star_length)) + self.name + ("*"*(self.star_length))

    self.string = self.title

    max_index = len(self.ledger)
    for index in range(max_index):
      self.lines = self.ledger[index]["description"][:23] # Max 23 characters of description
      
      self.lines = self.lines + (str('{:,.2f}'.format(self.ledger[index]["amount"]))).rjust(30 - len(self.lines)) # Format currency with xx.00

      self.string += "\n"
      self.string += self.lines

    self.string = self.string + "\n" + "Total: "+ str(self.funds)
    
    return self.string

def create_spend_chart(categories):
  total_string = "" # total_string to be returned at the end
  
  num_categories = len(categories)
  total_spent = 0
  for category in categories:
    total_spent = total_spent + category.spent

  for category in categories:
    category.fraction = (category.spent / total_spent) 
    category.fraction = math.floor(100*category.fraction)/100
    print(category.name, category.spent, category.fraction)

  names = [] # List of all names from the list used as the parameter
  for category in categories:
    names.append(category.name)
  max_length = len(max(names, key=len)) # Find length of longest string in names
  
  chart_title = 'Percentage spent by category'

  total_string = total_string + chart_title + "\n"

  percentage_string = ""
  # 0 to 100, each height is rounded down to nearest 10
  for percentage in range (100, -1, -10): 
    if percentage <= 90:  
      if percentage == 0:
        percentage_string = "  "+str(percentage)+"|"
      else:
        percentage_string = " "+str(percentage)+"|"
      # Loop through all categories to draw the "o"
      for category in categories:
        # For every percentage, check if fractional spent exceeds that percentage. Draw "o" if True
        if category.fraction >= (percentage/100) and percentage >= 10:
          # Checks to ensure "o" is drawn on correct category, otherwise will only be drawn on first category
          if names.index(category.name) == 0:
            percentage_string = percentage_string + " " + "o" + " "
          if names.index(category.name) == 1:
            percentage_string = percentage_string + "    " + "o" + " "
          if names.index(category.name) == 2:
            percentage_string = percentage_string + " " + "o" + " "
        elif category.fraction >= (percentage/100) and percentage < 10:
          percentage_string = percentage_string + " " + "o" + " "
    elif percentage == 100:
      percentage_string = str(percentage)+"|"
    total_string = total_string + percentage_string.ljust(14) +"\n"

  total_string = total_string + ("    "+"---"*num_categories+"-") + "\n"

  character_string = "     "
  extra_space = "     "
  
  for index in range (max_length):
    for category in categories:
      if index >= len(category.name) :
        character_string = character_string + "   "
      elif index < len(category.name) and index == max_length-1:
        character_string = character_string + "" + category.name[index] + "  "
      elif index < len(category.name):
        character_string = character_string + "" + category.name[index] + "  "
      else:
        return  
    if index < max_length-1:
      character_string = character_string + "\n" + extra_space

  # Scratch code For OLD CODE:
  # index = 0, character_string = "    " + " " + B {cat 1} + " "
  # index = 0, character_string = character_string+ " " + F {cat 2} + " " 
  # ...
  # index = 5, character_string = "    " + " " + n {cat 1} + " "
  # index = 5, character_string = character_string + " " + EMPTY {cat 2} + " " 
    # EMPTY needs to be "  " so that it is pushed to next category! 
    # Therefore, if index >= len(category.name): character_string = character_string + "   " {3 spaces}
  
  total_string = total_string + character_string
  print("Total String:" + "\n" + total_string)
  return total_string
  