import string

def check_password_strength(password):
    length=len(password)>=8
    lowercase=any(char.islower() for char in password)
    uppercase=any(char.isupper() for char in password)
    digit=any(char.isdigit() for char in password)
    special=any(char in string.punctuation for char in password)

    if all([length,lowercase,uppercase,digit,special]):
        return ("Strong Password")
    elif length and (lowercase or uppercase) and digit:
        return("Moderate Password")
    else:
        return("Weak Password")

def main():
    password=input("Enter your Password:  ")
    result=check_password_strength(password)
    print(f"Password Strength:  {result}")

main()