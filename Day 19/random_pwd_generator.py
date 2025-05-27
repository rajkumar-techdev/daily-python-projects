#Random Password  Generator with Custom options

import random
import string

def generate_password(length,use_upper,use_num,use_symbols):
    characters=list(string.ascii_lowercase)
    if use_upper:
        characters+=list(string.ascii_uppercase)
    if use_num:
        characters+=list(string.digits)
    if use_symbols:
        characters+=list("!@#$%^&*()_+{}[]>?<|")

    if not characters:
        print("No character type selected")

    password=''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("=== Password Generator ===")

    length=int(input("Enter password length: "))
    use_upper=input("Include Uppercase letters: (yes/no): ").lower()=='yes'
    use_num=input("Include Digits(yes/no): ").lower()=='yes'
    use_symbols=input("Include Symbols(yes/no): ").lower()=='yes'

    count=int(input("How many passwords to generate?: "))

    for i in range(count):
        pwd=generate_password(length, use_upper, use_num, use_symbols)
        print(f"Password {i+1}: {pwd}")

main()
