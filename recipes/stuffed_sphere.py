from pycraft_minetest import *

# Create a sphere of glass (so you can see through)
sphere(glass, 20, z=25)
# Now create a sphere of lava (but also water or sand could work)
# that will be generated inside the glass sphere
sphere(lava, 19, z=25)
