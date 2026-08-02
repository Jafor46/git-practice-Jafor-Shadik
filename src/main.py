from datetime import date
print('Name : Jafor Shadik')
today = date.today()
print("Today's Date :",today)

from utils import add, subtract, mul, div
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", mul(num1, num2))
    print("Division:", div(num1, num2))

except ValueError as error:
    print("Error:", error)

except Exception as error:
    print("Unexpected error:", error)

