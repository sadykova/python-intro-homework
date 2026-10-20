score = 100
#printing corresponding letter grade
def letter_grade(score):
    if (score >=90 and score <=100):
        print("Grade:A")
    elif (score >=80 and score <=89):
        print("Grade:B")
    elif (score >=70 and score <=79):
        print("Grade:C")
    elif (score >=60 and score <=69):
        print("Grade:D")
    else:
        print("Grade:F")

letter_grade(score)


