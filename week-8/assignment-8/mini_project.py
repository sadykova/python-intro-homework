#Defensive CSV Reader
import csv
import sys

clean_data =[]
skipped_rows = []
errors = []

total_rows = 0
parsed = 0
skipped = 0
try:
    #open and read the file
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    #go through each row
    for i, row in enumerate(rows, start=1):
        total_rows +=1

        if None in row:
            errors.append(f"Row {i}: extra column detected - skipped")
            continue

        try:
            amount = float(row["amount"])

            row["amount"] = amount
            clean_data.append(row)
            parsed +=1

        
        except ValueError as e:
            skipped_rows.append(row)
            errors.append(f"Row {i}: {e}")
            skipped +=1
        
        except KeyError as e:
            skipped_rows.append(row)
            errors.append(f"Row {i}: extra column detected - skipped")
            skipped +=1

    #Summary
    print("\n--- CSV REPORT ---")
    print(f"Rows attempted: {total_rows}")
    print(f"Rows parsed: {parsed}")
    print(f"Rows skipped: {skipped}")

    print("\nSkipped rows:")

    for error in errors:
        print(error)

    print("\nClean data: ")

    for row in clean_data:
        print(row)


except FileNotFoundError:
    print('Error: "messy_data.csv" was not found. Please check the file path and try again.')
    sys.exit()