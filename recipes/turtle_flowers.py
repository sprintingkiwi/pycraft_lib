from pycraft_minetest import *

# Create a Turtle object
kiki = Turtle([wool, random.randint(1, 12)])
# Set turtle speed
kiki.speed(11)


# Define how to make a quarter of a circle
def circle_quarter(steps):
    for i in range(90):
        kiki.forward(steps)
        kiki.right(1)


# Define how to make a petal
def petal(size):
    circle_quarter(size)
    kiki.right(90)
    circle_quarter(size)
    kiki.right(90)


# Define how to make a flower
def flower(size, petals):
    for i in range(petals):
        petal(size)
        kiki.right(360 / petals)


# Define how to make many flowers
def flowers(amount):
    for i in range(amount):
        kiki.penblock([wool, random.randint(1, 12)])
        flower(1, random.randint(3, 12))
        kiki.penup()
        pos = where()
        kiki.goto(0, -1, 0)
        kiki.pendown()


# Generate flowers calling the last function
flowers(10)
