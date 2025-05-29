

from forex_python.converter import CurrencyRates

def convert_currency():
    cr=CurrencyRates()

    from_currency=input("Enter currency to convert from (e.g. USD): ").upper()

    to_currency=input("Enter currency to convert to (e.g INR): ").upper()

    try:
        amount=float(input("Enter amount to convert: "))
        result=cr.convert(from_currency,to_currency,amount)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except Exception as e:
        print("Error" ,e)

convert_currency()