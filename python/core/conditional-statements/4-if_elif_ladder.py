"""
syntax:
if condition-1:
    # code of block execute if condition-1 is True
elif condition-2:
    # code of block execute if condition-2 is True
elif condition-3:
    # code of block execute if condition-3 is True
    .
    .
    .
else:
    # code of block execute if condition-1, condition-2, condition-3 is False  

"""

score = float(input("Enter your score: "))


if score >= 0 and score <= 100:
    if score >= 80:
        print("Grade: A")
    elif score >= 60:
        print("Grade: B")
    elif score >= 40:
        print("Grade: C")
    else:
        print("Sorry, You are not eligible for any class.")
else:
    print("Invalid score.\nPlease enter a valid score between 0 to 100.")

