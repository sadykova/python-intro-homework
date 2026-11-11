# Expense report generator
#import packages
import os
import csv
from datetime import datetime

#verify expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("Found it!")
else:
    print("Error: File not found.")

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
        writer = csv.writer(file)
        now = datetime.now()
        writer.writerow(f"Food Expense Report — generated today's date as {now.strftime('%B %d, %Y')}")
        for expense in food_expenses:
            writer.writerow(f"{expense['date']}: ${expense['amount']}" )
        writer.writerow(f"Total: {total:.2f}")




   
   
   

        
        

