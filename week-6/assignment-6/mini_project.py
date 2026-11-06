numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    """
    Finds the minimum 
    """
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
    
#print(find_min(numbers))

def find_max(numbers):
    """
    Finds the maximum
    """
    largest = float("-inf")
    for number in numbers:
        if number > largest:
            largest = number
    return largest
    

#print(find_max(numbers))
    
def search(numbers,target):
    """
    Performs a linear search for a target number
    """
    index = -1
    for i in range(len(numbers)):
        if numbers[i]==target:
            index=i
            break
    if index != -1:
        return index   
    else:
        print(f"'{target}' was not found in the list.")
        return -1
        
#print(search(numbers, 42))
        
def bubble_sort(numbers):
    """
    Performs the Bubble sort
    """
    n=len(numbers)
    reversed = numbers.copy()
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if reversed[j]>reversed[j+1]:
                reversed[j],reversed[j+1] = reversed[j+1],reversed[j]
                swapped=True
        if not swapped:
            break
    print(f"The reversed list is: {reversed}")
    return reversed

#print(bubble_sort(numbers))

def show_menu():
    """
    Displays the menu
    """
    print('''
    === Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit
 ''')
    option = int(input("Choose an option (1-5):"))
    return option

def main(numbers):
    """
    Coordinates the program based on user choice
    """
    while True:
        option=show_menu()  
        if option == 1:
           smallest=find_min(numbers)
           print(f"The smallest value is {smallest}.")
        elif option==2:
            largest=find_max(numbers)
            print(f"The largest value is {largest}.")
        elif option ==3:
            target = int(input("Enter a number to search for: "))
            index = search(numbers,target)
            if index != -1:
                print(f"Found '{target}' at index {index}")
            else:
                 print(f"'{target}' was not found in the list.")
        elif option==4:
            bubble_sort(numbers)
        elif option == 5:
            print("Program terminated.Thank you and Goodbye!")
            break


main(numbers)





