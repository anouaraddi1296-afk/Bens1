import random
import string

print("--- Password Generator ---")
length = int(input("Enter password length (e.g., 12): "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)

print(f"\nYour strong password is: {password}")
