"""
match variable:
    case pattern1:
        # action if variable matches pattern1
    case pattern2:
        # action if variable matches pattern2
    case _:
        # action if no pattern matches
"""

# 0 - Monday
# 6 - Sunday

import datetime

current_day = datetime.datetime.now().weekday()

match current_day:
    case 0:
        print("Today is Monday")
    case 1:
        print("Today is Tuesday")
    case 2:
        print("Today is Wednesday")
    case 3:
        print("Today is Thursday")
    case 4:
        print("Today is Friday")
    case 5:
        print("Today is Saturday")
    case 6:
        print("Today is Sunday")
    case _:
        print("Today is Invalid day")


# animal = input("Enter a animal name: ")
# match animal:
#     case "cat":
#         print("You chose a cat!")
#     case "dog":
#         print("You chose a dog!")
#     case "bird":
#         print("You chose a bird!")
#     case _:
#         print("Unknown animal!")