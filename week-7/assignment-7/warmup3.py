#use the os module
import os
#print current working directory
os.getcwd()

#check whether expenses.csv is in the current directory
if os.path.exists("expenses.csv"):
    print("Found it!")
else:
    print("File not found.")

#use os.path.join() to build the path
path = os.path.join("..","data", "expenses.csv")
print(path)