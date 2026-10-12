#Temperature converter
#Asking for user input
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit-32)*5/9
print(f"{fahrenheit:.1f} F is {celsius:.1f} C.")