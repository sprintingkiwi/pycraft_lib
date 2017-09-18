from pycraft_minetest import *

# Instance a Turtle object
uga = Turtle(obsidian)

# Create a variable for the side of the spiral
side = 1

while True:
    # Move the Turtle forward of "side" steps
    uga.forward(side)
    # Make the Turtle turn right of 90 (try to change it) degrees
    uga.down(90)
    # Increment the side variable
    side = side + 1
