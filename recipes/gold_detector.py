from pycraft_minetest import *

# Forever
while True:
    # If there is at least one block of gold
    # in a range of (default) 10 units around me...
    if near(gold):
        # Write it on the game chat
        chat("There is gold nearby!")
        # Delay
        time.sleep(1)
