numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print('''
    === Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit
 ''')
    option = int(input("Choose an option (1-5):"))
    min = float('inf')
    max = float("-inf")
    if option == 1:
        for number in numbers:
            if number < min:
                min = number
        print(f"The smallest value is {min}.")
        break
    if option == 2:
        for number in numbers:
            if number > max:
                max = number
        print(f"The biggest value is {max}.")
        break
    
    
