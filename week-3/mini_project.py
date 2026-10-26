day = input("What day is it?").lower()
time = input("What time of day?").lower()

def suggestions (day, time):
    if day == 'monday' and time == "morning":
        print("Monday morning is perfect for some Pilates!")
    elif day == "monday" and time == "afternoon":
        print("Monday afternoons are perfect to get some work done!")
    elif day == "monday" and time == "evening":
        print("Monday evenings are for family time!")
    elif day == "tuesday" and time == "morning":
        print("Tuesday mornings are perfect for sleeping in!")
    elif day == "tuesday" and time == "afternoon":
        print("Tuesday afternoons are for learning a language!")
    elif day == "tuesday" and time == "evening":
        print("Tuesday evenings are for yoga!")
    elif day == "friday" and time == "morning":
        print("Friday morning! Get a cup of tea with your bestie!")
    elif day == "friday" and time == "afternoon":
        print("Friday afternoon! Pack a backpack for weekend getaway!")
    elif day == "friday" and time == "evening":
        print("Friday evening! You arrived at your destination!")
    else:
        print("Sorry, I only have suggestions for Monday, Tuesday and Friday :(")
    
suggestions(day, time)
    