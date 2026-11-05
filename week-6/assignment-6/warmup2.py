#Functions and return values

def celsius_to_fahrenheit(c):
    '''
    Docstring for celsius_to_fahrenheit(c)
    
    :param c: converts Celsius to Fahrenheit using (c * 9/5) + 32

    '''
    return f"{c}C = {((c * 9/5) + 32):.1f}F"

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

def fahrenheit_to_celsius(f):
    '''
    Docstring for fahrenheit_to_celsius(f)
    
    :param c: converts Fahrenheit to Celsius using (f - 32) * 5/9

    '''
    return f"{f}F = {((f - 32) * 5/9):.1f}F"

print(fahrenheit_to_celsius(72))