from pycraft_minetest import *

# Create a Turtle object
pyr = Turtle(iron)

# Create a "steps" variable
steps = 10

# Repeat "half-steps" times
for i in range(steps/2):

    # Repeat 4 times (for 4 sides)
    for i in range(4):
        # Move the turtle forward "steps" steps
        pyr.forward(steps)
        # Make the turtle turn right 90 degrees
        pyr.right(90)

    # Make the turtle go up by one and inside the square by one,
    # each time returning to the original heading
    pyr.forward(1)
    pyr.right(90)
    pyr.forward(1)
    pyr.left(90)
    pyr.up(90)
    pyr.forward(1)
    pyr.down(90)

    # Decrease steps by two (one for each end of the sides)
    steps = steps - 2
