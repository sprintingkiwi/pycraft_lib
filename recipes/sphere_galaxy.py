from pycraft_minetest import *

for i in range(random.randint(50, 100)):
    sphere([wool, random.randint(0, 12)],
           random.randint(1, 30),
           x=random.randint(-200, 200),
           y=random.randint(-200, 200),
           z=random.randint(-200, 200))
