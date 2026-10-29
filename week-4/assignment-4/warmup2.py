# Dictionary operations
# add a record
student = {
    'name':'Sam', 
    'grade': 'B+',
    'subjects': ['Art','World History', 'International Relations 101']}


#print each key-value pari using .items() in a for loop
for key, value in student.items():
    print(f"Printing ... {key}: {value}")

# add a new key
student["graduated"] = False 
print(student)
