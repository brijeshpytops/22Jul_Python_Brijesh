# class Auth:
#     class Register:
#         def __init__(self, username, email, pwd, cpwd):
#             self.u = username # public
#             self.e = email
#             self.__p = pwd # private
#             self.c = cpwd

#         def is_email_valid(self):
#             if '.' in self.e and '@' in self.e:
#                 return True
#             else:
#                 return False 

#         def check_password(self):
#             if len(self.__p) >= 8:
#                 if self.__p == self.c:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
                
#         def register_user(self):
#             if self.is_email_valid():
#                 if self.check_password():
#                     print("User registered successfully.")
#                 else:
#                     print("Invalid data")
#             else:
#                 print("Invalid data")

# new_obj = Auth().Register("brijesh", "@.", "test1234", "test1234")
# print(new_obj.e)
# print(new_obj.__p)
# print(new_obj._Register__p)  # : _className__varName
# while(1):
#     username = input("Enter your username: ")
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     confirm_password = input("Enter your confirm passsword: ")
#     obj = Auth().Register(username, email, password, confirm_password)
#     obj.register_user()



# class ATM:
#     def __init__(self, pin):
#         self.__p = pin

#     def setPIN(self, atm_pin):
#         self.__p = atm_pin

#     def getPIN(self):
#         print(self.__p)

# obj = ATM("2222")
# obj.setPIN("1111")
# obj.getPIN()