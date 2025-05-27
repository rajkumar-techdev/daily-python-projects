
def currency_converter():

    print("=== Welcome to Currency Converter")
    print("1.INR to USD")
    print("2.INR to EUR")
    print("3.USD to INR")
    print("4.EUR to INR")

    choice=input("Enter your choice(1-4): ")
    amount=float(input("Enter amount:  "))

    if choice=='1':
        print(f"{amount} INR = {amount * 0.012} USD")
    elif choice=='2':
        print(f"{amount} INR = {amount * 0.011 } EUR")
    elif choice=='3':
        print(f"{amount} USD ={amount*83.0} INR")
    elif choice=='4':
        print(f"{amount} EUR = {amount*90.0} IND")
    else:
        print("Invalid choice")

currency_converter()