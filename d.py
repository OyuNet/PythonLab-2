age = int(input("Enter your age: "))
ticketprice = 3

if (age<6 or age>60):
    print("Your ticket is free.")
else:
    if (age>=6 and age<=18):
        print("Your ticket is {price} TL.".format(price = ticketprice/2))
    else:
        print("Your ticket is {price} TL.".format(price = ticketprice))