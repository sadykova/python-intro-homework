#Input valudation
#Ask for a positive number. If the user enters anything that is not a positive integer, print a message and ask again.
        
while True: 
    try:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            print(f"Got it: {number}")
            break
        else:
            print("That's not a positive number. Try again.")
    except ValueError:
        print("That's not a positive number. Try again.")