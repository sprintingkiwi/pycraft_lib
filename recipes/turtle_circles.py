from pycraft_minetest import *

# Create a Turtle object
uga = Turtle([wool, 0])
# Make our Turtle rotate up 90 degrees
uga.up(90)

# FOREVER
while True:

    # Repeat the following instructions 12 times
    # because the wool block has 12 different colors
    for color in range(12):

        # Set the block that our Turtle will use to draw - especially the color subtype
        uga.penblock([wool, color])

        # Repeat 18 times
        for i in range(18):
            # Move our Turtle forward
            uga.forward(5)
            # Make our Turtle turn up of 20 degrees (18 * 20 = 360)
            uga.up(20)

        # When a circle is complete, let's rotate other 30 degrees
        # so that we are ready to repeat all these steps and draw
        # another circle in a different position
        uga.up(30)
