import random
import string

def generate_password():

    length=int(input("Enter the desired password length: "))

    characters=string.ascii_letters+string.digits

    password="".join(random.choice(characters) for _ in range (length))

    print(f"Generated Password: {password}")

generate_password()
