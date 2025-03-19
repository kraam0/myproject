# addition == +
# subtraction == -
# multiplication == *
# division == /
operator = input("entre an operator + - / * : ")
number1 = float(input("entre the first number : "))
number2 = float(input("entre the second number : "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("you didnt entre an operator")  