#Validate numeric input
while True:
    try:
        num = float(input("Enter a number: "))
    except ValueError: 
        print("That's not a valid number. Try again.")
    else:
        print(f"You entered: {num}")
        break