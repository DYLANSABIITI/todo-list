import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#"


number = int(input("How many passwords: "))
length = int(input("Length of password: "))

for num in range(number):
    password = ''
    for passw in range(length):
        password += random.choice(chars)
    print(password)