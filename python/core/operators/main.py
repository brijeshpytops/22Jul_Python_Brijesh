"""
Link : https://learningmonkey.in/wp-content/uploads/2021/05/Operator-Precedence-and-Associativity-in-Python.jpg

What is operators in python?
=====================================


Operators in Python are special symbols or keywords that perform operations on variables and values. They are used to manipulate data and variables, enabling you to perform computations, comparisons, and logical operations.


Arithmetic Operators: Used to perform mathematical operations.

+ : Addition
- : Subtraction
* : Multiplication
/ : Division
% : Modulus
** : Exponentiation
// : Floor Division

Comparison Operators: Used to compare two values.

== : Equal to
!= : Not equal to
> : Greater than
< : Less than
>= : Greater than or equal to
<= : Less than or equal to

Logical Operators: Used to combine conditional statements.

and : Returns True if both statements are true
or : Returns True if one of the statements is true
not : Reverses the result, returns False if the result is true

Bitwise Operators: Used to perform bit-level operations.

& : AND
| : OR
^ : XOR
~ : NOT
<< : Zero fill left shift
>> : Signed right shift

Assignment Operators: Used to assign values to variables.

= : Assign
+= : Add and assign
-= : Subtract and assign
*= : Multiply and assign
/= : Divide and assign
%= : Modulus and assign
**= : Exponentiation and assign
//= : Floor division and assign

Identity Operators: Used to compare the objects, not if they are equal, but if they are actually the same object.

is : Returns True if both variables are the same object
is not : Returns True if both variables are not the same object

Membership Operators: Used to test if a sequence is presented in an object.

in : Returns True if a sequence with the specified value is present in the object
not in : Returns True if a sequence with the specified value is not present in the object
"""

# Arithmetic Operators

num1 = 10
num2 = 5

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)
# print(num1**num2)
# print(num1//num2)


# Assignment/shorthand Operators:
num1 = 10

# num1 = num1 + 20
# num1 += 20
# num1 -= 20
# num1 *= 20
# num1 /= 20
# num1 **= 20
# num1 //= 20

# print(num1)


# Comparison Operators:

# num1 = 10
# num2 = 20
# num3 = 30

# print(num1 == num2)
# print(num1 != num2)
# print(num1 < num3)
# print(num1 > num3)
# print(num1 >= num3)
# print(num1 <= num3)


# Identity Operators:

# num1 = 10
# num2 = 20
# num3 = '10'

# print(num1 is num2)
# print(num1 is num3)
# print(num1 is not num3)

# Membership Operators:

# code = "python"
# print('p' in code)
# print('py' in code)
# print('Py' in code)
# print('Py' not in code)
# print('pto' in code)

# Logical Operators: 

# and, or, not

# A B C and or
# T T T T   T
# F T T F   T
# T F T F   T
# T T F F   T
# F F F F   F

# A not
# T F
# F T

c1 = True
c2 = False
c3 = 23 < 50
c4 = 23 > 2
c5 = 0
c6 = 1

# print(c1 and c2) # False
# print(c1 and c3) # True
# print(c1 and c4) # True
# print(c1 and c2 or c3) # True
# print(c1 and c2 or c3 and c4) # True



# Bitwise Operators:
# 2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
# 128 64  32  16  8   4   2   1

# Dec - 1 -> Bin 0001
# Dec - 3 -> Bin 0011
# Dec - 5 -> Bin 0101
# Dec - 6 -> Bin 0110
# Dec - 7 -> Bin 0111
# Dec - 17 -> Bin 10001

A = 3
B = 5

print(A & B)
print(A | B)
print(A ^ B)

# 0 - False
# 1 - True

# 3 5
# A B & | ^ !
# -----------
# 0 0 0 0 0 1
# 0 1 0 1 1 1
# 1 0 0 1 1 0
# 1 1 1 1 0 0

x = 7
# 7 - 00000111
# 56 - 00111000
# 112 - 01110000

# 32
# 16
# 08
# --
# 56
x = x << 3
x = x << 1

print(x)