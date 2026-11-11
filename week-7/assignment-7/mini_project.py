# Expense report generator
#import packages
import os
import csv
from datetime import datetime
import sys

#verify expenses.csv exists

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    sys.exit()

# read the file into a list of dictionaries
with open('../data/expenses.csv','r') as file:
    reader = csv.DictReader(file)
    food_expenses = []
    total = 0
    for row in reader:
        row['amount'] = float(row['amount'])
        if row["category"] == "Food":
            food_expenses.append(row)
    for expense in food_expenses:
        total += expense['amount']
    print(food_expenses)
    print(type(row['amount']))
    print(total)

    with open('food_report.txt', 'w', newline ='') as file:
        now = datetime.now()
        file.write(f"Food Expense Report — generated {now.strftime('%B %d, %Y')}\n")
        for expense in food_expenses:
            file.write(f"{expense['date']}: ${expense['amount']}\n" )
        file.write(f"Total: ${total:.2f}\n")




   
   
   

        
        

