"""
- Enter first number,
- Enter type of operator
- Enter second number
- calculator logic
- Print results
"""


num1 = float(input("Enter first number: "))
operator = input("Select an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator != "+" or operator != "-" or operator != "*" or operator != "/":
    print("you have to select a valid operator")
else:
    print(num1 / num2)
