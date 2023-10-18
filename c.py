gpa = float(input("Enter your GPA: "))
lectures = int(input("Enter your lectures count: "))

if (gpa >= 2.0):
    if (lectures >= 47):
        print("Graduated!")
    else:
        print("Not enough number of lectures.")
else:
    if (lectures >= 47):
        print("Not enough GPA!")
    else:
        print("Not enough number of lectures and GPA!")