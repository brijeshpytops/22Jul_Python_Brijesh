"""
Datatypes:

What is datatypes?
==================
A datatype is a classification that specifies which type of value a variable can hold and what operations can be performed on it. Python supports various built-in datatypes, including:

                            Datatype
                                |
              ------------------------------------                           
              |                                  |
           prmitive                       non-primitive
       -----------------           ----------------------------
       |               |           |             |            |
Numeric-types    Boolean-type Sequence-types Mapping-type Set-types
 -------------         -       ----------        -            -
 |    |      |         |       |   |    |        |            |
int float complex     bool    str list tuple    dict         set


# Binary Types:

# bytes: Immutable sequences of bytes.
# bytearray: Mutable sequences of bytes.
# memoryview: A view object that exposes the buffer interface.

"""

age = 24
# print(type(age))

price = 345.78
# print(type(price))

real_img = 34 + 356532j
# print(type(real_img))

is_active = False
# print(type(is_active)) # <class 'bool'>

name = "tops"
# print(type(name)) # <class 'str'>

names = ['k', 'n', 'v', 'p', 'm']
# print(type(names)) # <class 'list'>

nums = (1,2,3)
# print(type(nums)) # <class 'tuple'>

car = {
    "brand": "Ford",
    "price": "45L"
}
# print(type(car)) # <class 'dict'>

ch = {'a', 'b', 'c'}
# print(type(ch)) # <class 'set'>

CH = {}
# print(type(CH)) # <class 'dict'>

# TYPE CONVERSION
# int() - converts to integer
# float() - converts to float
# complex() - converts to complex number
# ...

# Implicit coversion
# num1 = 10
# num2 = 10.5
# num3 = num1 + num2
# print(num3)


# Explicit coversion
# num1 = 10
# num2 = 10.5
# num3 = int(num2)
# print(type(num3))

# name = "dsghfd"
# i = int(name) # ValueError: invalid literal for int() with base 10: 'dsghfd'
# print(type(i))

# nums = "534265"
# print(type(int(nums))) # 534265