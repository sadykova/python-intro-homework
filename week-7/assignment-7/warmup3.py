#use the os module
import os
#print current working directory
print(os.getcwd())

#check whether expenses.csv is in the current directory
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#use os.path.join() to build the path
path = os.path.join("..","data", "expenses.csv")
print(path)