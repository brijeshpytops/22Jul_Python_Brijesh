"""
syntax:

for var in itrable_var/squence:
    # block of code
"""

# for num in range(1, 11):
#     print(num)

# for num in range(1, 11, 2):
#     print(num)

# for num in range(2, 11, 2):
#     print(num)

# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num, "Even")
#     else:
#         print(num, "Odd")

# for ch in "Tops technology pvt. ltd.":
#     print(ch)

# for num in range(1, 6):
#     print("*", end=' ')
#     print("*", end=' ')
#     print("*", end=' ')
#     print("*", end=' ')
#     print("*", end=' ')
#     print("\n")

# num = 5
# for row in range(1, num + 1):
#     for col in range(1, num + 1):
#         print("*", end=' ')
#     print()

# num = 5
# for row in range(1, num + 1):
#     for col in range(1, row + 1):
#         print("*", end=' ')
#     print()

# num = 5
# for row in range(1, num + 1):
#     for col in range(num-row+1, 0, -1):
#         print("*", end=' ')
#     print()


# num = 5
# for row in range(1, num + 1):
#     for col in range(1, row + 1):
#         print("*", end=' ')
#     print()

# for row in range(1, num + 1):
#     for col in range(num-row, 0, -1):
#         print("*", end=' ')
#     print()

# num = 5
# for row in range(1, num + 1):
#     for col in range(num-row, 0, -1):
#         print(" ", end=' ')
#     for col in range(1, row + 1):
#         print("*", end=' ')
#     print()


# num = 10
# for row in range(1, num + 1):
#     for col in range(num-row, 0, -1):
#         print(" ", end=' ')
#     for col in range(1, row + 1):
#         print("*", end=' ')
#     for col in range(1, row):
#         print("*", end=' ')
#     print()
# for row in range(1, num + 1):
#     for col in range(1, row+1):
#         print(" ", end=' ')
#     for col in range(num-row, 0, -1):
#         print("*", end=' ')
#     for col in range(num-row-1, 0, -1):
#         print("*", end=' ')
#     print()

# * * * * * * * * *
#     *   *   *   *
#         *   *   *   
#         *   *   *
#             *   *   
#             *   *   
#             *   *   
#                 *
#                 *


num = 9
for row in range(1, num + 1):
    for col in range(1, row + 1):
        if row % 2 == 0:
            if col == 1:
                print("*", end=' ')
                continue
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print()