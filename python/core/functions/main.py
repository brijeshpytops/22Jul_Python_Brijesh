"""
syntax:

def function_name(para1, para2..paran):
    block of code

function call
function_name(value1, value2,....,valuen)

"""

# a = 10
# b = 20
# c = a + b
# print(c)

# d = 30
# e = 40 
# f = d + e

# def add(a, b):
#     print(a + b)

# add(10, 20)
# add(30, 40)


# def add(a, b):
#     return a + b

# print(add(30, 40))

# types of paras
# 1] positional para
# 2] default/ keyword para
# 3] variable length para
#     - *args
#     - **kwargs

# 1] positional para
def add(a, b, c):
    print(a + b + c)

# add(10, 20, 30)

# 2] default/ keyword para
# def bill(tomato, potato=50):
#     print("Tomato price is: ", tomato)
#     print("Potato price is: ", potato)
#     print("Total amount: ", tomato + potato)

# bill(30)

# 3] variable length para
#     - *args
#     - **kwargs
# def add(*nums):
#     print(sum(nums))
#     # print(type(nums))

# add(1,2,3,4, 100, 1000)

# def bill(**products):
#     # print(type(products))
#     total = 0
#     for key, value in products.items():
#         print(f"{key} price is: {value}")
#         total += value

#     print("Total amount is: ", total)

# bill(pen=10, book= 200, tomato=30, iceCream=20)

# a = 10 # global

# def test():
#     global a 
#     a = 20 # local
#     print(a)

# test()
# print(a)

# def upper_case(func):
#     def wrapper():
#         res = func().upper()
#         print(res)
#         return res
#     return wrapper

# def capitalize_case(func):
#     def wrapper():
#         res = func().capitalize()
#         print(res)
#         return res
#     return wrapper

# @capitalize_case
# @upper_case
# def text():
#     return input("Enter something: ")

# text()

# test = lambda num1, num2:num1*num2
# print(test(10, 20))

nums = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x*x, nums)))
# print(list(filter(lambda x:x%2==0, nums)))
# print(list(filter(lambda x:x%2!=0, nums)))

# def word_counter(func):
#     def wrapper():
#         res = func()
#         print("Total words: ", len(res.split()))
#         return res
#     return wrapper

# @word_counter
# def test():
#     return input("Enter something: ")

# print(test())
