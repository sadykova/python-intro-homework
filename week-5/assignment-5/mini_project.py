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
    smallest = float('inf')
    largest = float("-inf")
    if option == 1:
        for number in numbers:
            if number < smallest:
                smallest = number
        print(f"The smallest value is {smallest}.")
    elif option == 2:
        for number in numbers:
            if number > largest:
                largest = number
        print(f"The biggest value is {largest}.")
    elif option == 3:
        target = int(input("Enter a number to search for: "))
        index = -1
        for i in range(len(numbers)):
            if numbers[i]==target:
                index=i
                break
        if index != -1:
            print(f"Found '{target}' at index {index}")
        else:
            print(f"'{target}' was not found in the list.")
    elif option == 4:
        n=len(numbers)
        for i in range(n-1):
            swapped=False
            for j in range(n-i-1):
                if numbers[j]>numbers[j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                    swapped=True
            if not swapped:
                break
        print(numbers)
    elif option == 5:
        print("Program terminated.Thank you and Goodbye!")
        break
   
        



    
    
