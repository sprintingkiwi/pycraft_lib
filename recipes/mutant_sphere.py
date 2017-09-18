from pycraft_minetest import *

# Store player position in a variable
pos = where()
# Write on chat that position (just as a test)
chat(pos)

# Forever
while True:

    # Sequentially create many spheres with different materials
    # but in the same absolute position
    sphere(grass, 10, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)
    sphere(gold, 10, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)
    sphere(ice, 10, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)
