# list operations
numbers = [100,55, 87,44,36,67,64,88]

#print the first item
print(f"First:{numbers[0]}")
#print the last item using a negative index
print(f"Last:{numbers[-1]}")
#print a slice containing only the middle four items
print(f"Middle:{numbers[2:6]}")
#print a full list in reverse order
numbers.reverse()
print(f"Reversed: {numbers}")