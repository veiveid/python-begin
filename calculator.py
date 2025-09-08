# -*- coding: UTF-8 -*-

# caculator（command line）
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: divide by zero"
    return a / b

def calculator():
    print("=== welcome use this calculator ===")
    print("operator that supported：+  -  *  /")
    print("input 'q' to quit.")

    while True:
        # input the first numer
        num1 = input("\nPlease enter the first number: ")
        if num1 == "q":
            print("Program terminated. Goodbye.")
            break
        if not num1.replace(".", "", 1).isdigit():
            print("Invalid number. Please try again.")
            continue
        num1 = float(num1)

        # input operator
        operator = input("Please enter the operator: (+, -, *, /)： ")
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            continue

        # 输入第二个数字
        num2 = input("Please enter the second number: ")
        if not num2.replace(".", "", 1).isdigit():
            print("Invalid number. Please try again.")
            continue
        num2 = float(num2)

        # execute
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)

        print(f"result：{num1}{operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()

