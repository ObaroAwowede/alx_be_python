num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

ask = str(input("Choose the operation (+, -, *, /):"))

if ask == "+":
    result = num1 + num2
    print("the result is ", result)
if ask == "-":
    result = num1 - num2
    print("the result is ", result)
if ask == "/":
    result = num1 / num2
    print("the result is ", result)
if ask == "*":
    result = num1 * num2
    print("the result is ", result)
