import random
import string

def password_generated(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range (length))
    return password

length = int(input("Enter length of password to be generated: "))
password = password_generated(length)
print(f"Generated Password: {password}")