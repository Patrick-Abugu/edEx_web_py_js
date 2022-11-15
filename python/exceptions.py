import sys
try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
except ValueError:
    print("Please enter a valid number")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error! Cannot divide by zerro")
else:
    print(f"{x}/{y} = {x/y}")