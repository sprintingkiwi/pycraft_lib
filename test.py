from pycraft_minetest import *

pos = where()
chat(pos)

maze("maze1.csv")

t = turtle(obsidian)
t.forward(10)

move(3, 10, 5)

chat(where())

sphere(ice, y=-20)

circle([wool, 5], direction="horizontal")

line(gold, 0, 0, 0, 0, 50, 0)

block(iron, y=3)

blocks(wood, x=5, y=6, z=10)

size = readnumber("tell the size...")

cube(redstone, size)

text = readstring("say something...")

chat("I said: " + text)

pyramid(sandstone)

polygon(obsidian, 12, 30)

chat("Hello Minecraft!")

color = 0

uga = turtle([wool, color])

while True:

    for i in range(18):
        uga.forward(5)
        uga.up(20)
    uga.up(30)
    color += 1
    uga.penblock([wool, color % 12])


# GOLD in ICE
# while True:
#     if over(ice):
#         chat("ice")
#         block(gold, y=-1)
#     if near(gold):
#         chat("gold nearby!")


# TURTLE LOOP
# uga = turtle(redstone)
# passi = 2
# while True:
#     uga.forward(passi)
#     uga.left(90)
#     passi = passi + 2

# uga = turtle(redstone)
# bea = turtle(beacon)
# bea.setposition(0, 1, 0)
# # col = turtle(beacon)
#
# while True:
#     uga.forward(1)
#     bea.forward(1)

# uga = turtle(redstone)
# bea = turtle(powered_rail)
# bea.setposition(0, 1, 0)
# # col = turtle(beacon)
#
# while True:
#     uga.forward(2)
#     bea.forward(1)



# ANIMATE CUBE
# x = pos.x
# y = pos.y
# z = pos.z
# while True:
#     cube(ice, 5, x, y, z, absolute=True)
#     move(x-5, y+1, z+2, absolute=True)
#     time.sleep(0.1)
#     cube(air, 5, x, y, z, absolute=True)
#     x += 1

