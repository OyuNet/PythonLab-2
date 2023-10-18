import math
print("This app calculates roots of ax2 + bx + c\nPlease enter your values.")

a = float(input("A = ?: "))
b = float(input("B = ?: "))
c = float(input("C = ?: "))

discriminant = float(b**2-4*a*c)

if (discriminant > 0):
    firstRoot = (-b+(math.sqrt(discriminant)))/2*a
    secondRoot = (-b-(math.sqrt(discriminant)))/2*a
    print("Your roots are: {firstRoot}, {secondRoot}".format(firstRoot = firstRoot, secondRoot = secondRoot))
elif (discriminant == 0):
    root = (-b+(math.sqrt(discriminant)))/2*a
    print("Your root is {root}".format(root = root))
else:
    print("You don't have root.")