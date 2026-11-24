#handle a missing file
try:
    with open("../data/missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')