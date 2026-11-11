#read a tex file line by line
with open("../data/notes.txt", 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        print(f"Line {i+1}: {lines[i]}".strip())

    
    