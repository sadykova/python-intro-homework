# Data
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer using a loop

top_name = None
top_score = float('-inf')

for student in students:
    if student["score"]>top_score:
        top_score = student["score"]
        top_name = student["name"]

print(f"Top scorer: {top_name} ({top_score})")

#Calculate the class average
sum_scores = 0

for student in students:
    sum_scores +=student["score"]
avg = sum_scores/len(students)
print(f"Class average: {avg}")

#List all unique subjects
unique = set()

for student in students:
    unique.add(student['subject'])
print(f"Subjects offered: {unique}")

#List high scores
high_scores = []

for student in students:
    if student['score']>75:
        high_scores.append(student['name'])

print(f"High scores: {high_scores}")

