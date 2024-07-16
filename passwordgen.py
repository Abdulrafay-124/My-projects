import secrets
import string
import random

letters = string.ascii_letters
digits = string.digits
special_charcters = string.punctuation
selection_list  = letters + digits + special_charcters

length = 10

password = " "

for i in range(length):
    password += "".join(secrets.choice(selection_list))

print(password)




