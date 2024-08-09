"""
syntax:
if condition1:
    if condition2:
        # block of code

if condition1:
    if condition2:
        # block of code
    else:
        # block of code
else:
    # code of block

"""

age = int(input("Enter your age: "))

"""
age >= 18
weight >= 50
"""

if age >= 18:
    weight = float(input("Enter your weight: "))
    if weight >= 50:
        print("You are eligible for the job")
    else:
        print("You are not eligible for the job")
else:
    print("You are not eligible for the job")
