"""
syntax:
if condition:
    # code of block execute if condition is True
"""

bal = 10000
wb = 50000

if wb <= bal:
    print("You can withdraw")
    print("Withdrow successfully done.")
    print("Total remaining amount is: ", bal-wb)