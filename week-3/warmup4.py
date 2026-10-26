number = int(input("Enter a number:"))

def sign(number):
    if number == 0:
        print(f"{number} is zero.")
    elif number >0:
        print(f"{number} is positive.")
    else:
        print(f"{number} is negative." )    

def parity(number):
    if number == 0:
        print(f"{number} is even.")
    elif number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd." )   

sign(number)
parity(number)
