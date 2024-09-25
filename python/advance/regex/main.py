import re

# data = "dfkljiu; xmṁ,cwaefvidsfṁfhe p fc 23-12-1996 dfkljiu; xmṁ,cwaefvidsfṁfhep +91 536-876-5345 raj.shah@gmail.com fc dfkljiu; xmṁ,c'waefvidsfṁfhep fc 1-1-2000 dfkljiu; tops.help@tops.com xmṁ,cwaefvidsfṁfhep fc 05/2/2005 ,jhgrbvhhg brijesh@gmail.com uyfuhgiyuer ;jvjuf7ljfghkyudt"



# date_pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'

# print(re.findall(date_pattern, data))

# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# print(re.findall(email_pattern, data))

# data = "+91 536-876-5345"
# # Pattern for phone numbers like +915368765345 (no spaces or hyphens)
# phone_pattern = r'\b\d{1,3} \d{3}-\d{3}-\d{4}\b'

# # Extracting the phone number
# phone_numbers = re.findall(phone_pattern, data)

# # Print the extracted phone numbers
# print(phone_numbers)


# data = "surat is a small city"
# print(re.sub("small", "large", data))


# data = "91 536-876-5345"
# phone_pattern = r'\b\d{1,3} \d{3}-\d{3}-\d{4}\b'

# res = re.match(phone_pattern, data)
# print(res)
# print(res.group())

# res = re.search(phone_pattern, data)
# print(res)
# print(res.group())


import re

# List of phone numbers in different formats
numbers_list = [
    "+91 536-876-5345",
    "+91 5368765345",
    "+915368765345",
    "+91 (536) 876-5345",
    "+91-536-876-5345",
    "536-876-5345",  # Without country code
    "091-536-876-5345",  # With leading 0
]

# Flexible pattern for various phone number formats
phone_pattern = r'\b\+?\d{1,3}[-\s.]?(\(?\d{1,4}\)?)?[-\s.]?\d{1,4}[-\s.]?\d{1,4}[-\s.]?\d{1,9}\b'

# Iterate through the list and check each number
for number in numbers_list:
    if re.match(phone_pattern, number):
        print(f"Matched: {number}")
    else:
        print(f"Not matched: {number}")
