# class className:
    # block of code

# obj_name = className()

# num1 = 10
# num2 = 20

# def add():
#     res = num1 + num2
#     print(res)

# print(num1)
# print(num2)
# add()

# class Math:
#     # data member - (attributes and properties)
#     num1 = 10
#     num2 = 20

#     # member function - (functions and methods)
#     def add(self):
#         res = self.num1 + self.num2
#         print(res)

# obj = Math()
# print(obj.num1)
# print(obj.num2)
# obj.add()

class Auth:
    class Register:
        def user_register(self):
            print("Your registration has been successfully done.")

reg_obj = Auth().Register()
reg_obj.user_register()