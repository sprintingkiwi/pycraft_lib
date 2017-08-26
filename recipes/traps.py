from pycraft_minetest import *

# FOREVER
while True:
    # If you're stepping on a block of diamond...
    if over(diamond):
        # Then create a lava sphere around you!
        sphere(lava, 2)
