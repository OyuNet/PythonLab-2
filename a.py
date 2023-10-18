import math

value = float(input("Enter your number: "))
if (value < 0):
    value = value**2
    value = math.sqrt(value)
    print("Your number's absolute value is",value)
else:
    print("Your number's absolute value is",value)
    