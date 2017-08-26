from pycraft_minetest import *


while True:

    # For each number in a range
    for color in range(12):
        # Create a cube of wool blocks
        # with that number as block-subtype
        cube([wool, color], 4, x=-2, y=-5, z=-2)

    # Delay
    time.sleep(0.1)
