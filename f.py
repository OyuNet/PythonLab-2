# PS: I hate turtle...
import turtle

tortuga = turtle.Turtle()
size = int(input("Enter the size of shape: "))

if (size < 40):
    tortuga.circle(size)
else:
    tortuga.forward(size)
    tortuga.right(90)
    tortuga.forward(size)
    tortuga.right(90)
    tortuga.forward(size)
    tortuga.right(90)
    tortuga.forward(size)
    tortuga.right(90)