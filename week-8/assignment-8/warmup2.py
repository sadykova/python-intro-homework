#Safe division
try:
    num = int(input("Enter the numerator: "))
    denom = int(input("Enter the denominator: "))
    print(f"{num}/{denom}={num/denom}")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")
