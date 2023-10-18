num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if (num1 < num2):
    if (num1 < num3):
        print("Lowest value is",num1)
    else:
        print("Lowest value is",num3)
else:
    if (num2 < num3):
        print("Lowest value is",num2)
    else:
        print("Lowest value is", num3)