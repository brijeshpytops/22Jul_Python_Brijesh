"""
What is string in python?
=====================================
A string in Python is a sequence of characters, such as a word or a phrase. Strings are immutable, meaning they cannot be changed after they are created.

including in string: a-z, A-Z, 0-9, special symbols.

syntax:
str_name = ''
str_name = ""
str_name = ''''''
"""

# str_name = ''
# print(type(str_name))
# str_name = ""
# print(type(str_name))
# str_name = ''''''
# print(type(str_name))
# str_name = """"""
# print(type(str_name))

name = "tops TECHNOLOGIES PVT. LTD."
# print(len(name))

# Access a string

# accsess full string
# print(name)

# INDEXING (+/-)    
# print(name[0])
# print(name[9])
# print(name[-1])
# print(name[-6])

# SLICING [+/-]
# Syntax: obj_name[start:stop+1:step+1]
# print(name[0:6])
# print(name[::2])
# print(name[::3])

# print(name[::-1])
# print(name[::-1][23:])
# print(name[-4:-12:-1])

# "Your OTP is : 2463"

book = "java"
price = 35265.5464
pages = 2354
# print("Book name is python and price is 35265.5464 and pages are 2354")
# print(f"Book name is {book} and price is {price} and pages are {pages}")
# print("Book name is {} and price is {} and pages are {}".format(book, price, pages))
# print("Book name is {1} and price is {0} and pages are {2}".format(book, price, pages))
# print("Book name is %s and price is %.2f and pages are %d" % (book, price, pages))

# print("my name is "Brijesh gondaliya"")
# print("my name is 'Brijesh gondaliya'")
# print('my name is "Brijesh gondaliya"')
# print("my name is \"Brijesh gondaliya\"")

# print("\\\\")
# print("\"")
# print("\'")
# print("\n")
# print("\t")
# print("\b")

# print("Brijesh go\\ndaliya")
# print(r"Brijesh go\ndaliya")

company = "     TopS    TeCHnoLOGy Pvt. LTd.    "
# print(dir(company))
# print(company.lower())
# print(company.upper())
# print(company.swapcase())
# print(company.title())
# print(company.capitalize())

# print(company.lstrip())
# print(company.rstrip())
# print(company.strip())
# print(company.title().strip().replace("  ", " ").replace("  ", " "))

code = "python"
# print(code.center(19,"-"))

# print(code.startswith("p"))
# print(code.startswith("P"))
# print(code.endswith("ON"))
# print(code.endswith("on"))

password = "Tops@123"
upr = False
m_upr = True
lwr = False
m_lwr = True
sc = False
m_sc = True
di = False
m_di = True

if len(password >= 8):
    for ch in password:
        # print(ch)
        if ch.isupper():
            upr = True
        else:
            if m_upr:
                print("Atleast only one char must be upper case.")
                m_upr = False
        if ch.islower():
            lwr = True
        else:
            if m_lwr:
                print("Atleast only one char must be lower case.")
                m_lwr = False
        if not ch.isalnum():
            sc = True
        else:
            if m_sc:
                print("Atleast one special char must be there.")
                m_sc = False
        if ch.isdigit():
            di = True
        else:
            if m_di:
                print("Atleast only one digit must be there.")
                m_di = False

if upr and lwr and sc and di:
    print("Strong Password")
else:
    print("Weak Password")






