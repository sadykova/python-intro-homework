#Validation Function

def is_valid_score(score):
    if 0<=score<=100:
        return True
    else:
        return False 
    
#print(is_valid_score(95))

test_score = int(input("Enter a score: "))

if is_valid_score(test_score):
    print("Valid score")
else:
    print("Invalid score - must be between 0 and 100.")