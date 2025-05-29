#Simple Calculator

def simple_calculator():
    print("Simple Calculator")

    try:
        num1=float(input("Enter First number: "))
        num2=float(input("Enter second number: "))

        print("Select Operations: add,sub,mul,div")
        op=input("Enter operation: ")

        if op =='add':
            result=num1+num2
        elif op=='sub':
            result=num1-num2
        elif op=='mul':
            result=num1*num2
        elif op=='div':
            if num2!=0:
                result=num1/num2
            else:
                print("Error,Division by Zero")
        else:
            print("Invalid Opereation")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid Input,Please enter numbers.")
simple_calculator()