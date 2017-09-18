import time, random, math, os
import connection
import blocklist as bl
from util import *
from event import *
conn = connection.Connection("localhost", 4711)

LIBRARY_VERSION = 0.5

# Find the player
# players = mc.getPlayerEntityIds()

# Wait for at least one player

wait_for_player = True
while wait_for_player:
    try:
        ids = conn.sendReceive("world.getPlayerIds")
    except:
        print("Waiting for a player to connect...")
        time.sleep(1)
    else:
        wait_for_player = False

players = map(int, ids.split("|"))
player = players[0]

# BLOCKS
air = bl.AIR.id
stone = bl.STONE.id
grass = bl.GRASS.id
dirt = bl.DIRT.id
cobblestone = bl.COBBLESTONE.id
wood_planks = bl.WOOD_PLANKS.id
sapling = bl.SAPLING.id
bedrock = bl.BEDROCK.id
water_flowing = bl.WATER_FLOWING.id
water = bl.WATER.id
water_stationary = bl.WATER_STATIONARY.id
lava_flowing = bl.LAVA_FLOWING.id
lava = bl.LAVA.id
lava_stationary = bl.LAVA_STATIONARY.id
sand = bl.SAND.id
gravel = bl.GRAVEL.id
gold_ore = bl.GOLD_ORE.id
iron_ore = bl.IRON_ORE.id
coal_ore = bl.COAL_ORE.id
wood = bl.WOOD.id
leaves = bl.LEAVES.id
glass = bl.GLASS.id
lapis_lazuli_ore = bl.LAPIS_LAZULI_ORE.id
lapis_lazuli = bl.LAPIS_LAZULI_BLOCK.id
sandstone = bl.SANDSTONE.id
bed = bl.BED.id
cobweb = bl.COBWEB.id
grass_tall = bl.GRASS_TALL.id
wool = bl.WOOL.id
flower_yellow = bl.FLOWER_YELLOW.id
flower_cyan = bl.FLOWER_CYAN.id
mushroom_brown = bl.MUSHROOM_BROWN.id
mushroom_red = bl.MUSHROOM_RED.id
gold = bl.GOLD_BLOCK.id
iron = bl.IRON_BLOCK.id
stone_slab_double = bl.STONE_SLAB_DOUBLE.id
stone_slab = bl.STONE_SLAB.id
brick = bl.BRICK_BLOCK.id
tnt = bl.TNT.id
bookshelf = bl.BOOKSHELF.id
moss_stone = bl.MOSS_STONE.id
obsidian = bl.OBSIDIAN.id
torch = bl.TORCH.id
fire = bl.FIRE.id
stairs_wood = bl.STAIRS_WOOD.id
chest = bl.CHEST.id
diamond_ore = bl.DIAMOND_ORE.id
diamond = bl.DIAMOND_BLOCK.id
crafting_table = bl.CRAFTING_TABLE.id
farmland = bl.FARMLAND.id
furnace_inactive = bl.FURNACE_INACTIVE.id
furnace_active = bl.FURNACE_ACTIVE.id
door_wood = bl.DOOR_WOOD.id
ladder = bl.LADDER.id
stairs_cobblestone = bl.STAIRS_COBBLESTONE.id
door_iron = bl.DOOR_IRON.id
redstone_ore = bl.REDSTONE_ORE.id
ice = bl.ICE.id
snow = bl.SNOW_BLOCK.id
cactus = bl.CACTUS.id
clay = bl.CLAY.id
sugar_cane = bl.SUGAR_CANE.id
fence = bl.FENCE.id
glowstone = bl.GLOWSTONE_BLOCK.id
stone_brick = bl.STONE_BRICK.id
glass_pane = bl.GLASS_PANE.id
melon = bl.MELON.id
fence_gate = bl.FENCE_GATE.id
glowing_obsidian = bl.GLOWING_OBSIDIAN.id
nether_reactor_core = bl.NETHER_REACTOR_CORE.id
#monster_spawner = bl.MONSTER_SPAWNER.id
#standing_sign = bl.STANDING_SIGN_BLOCK.id
#rail = bl.RAIL.id
#lever = bl.LEVER.id
#sponge = bl.SPONGE.id
#pumpkin = bl.PUMPKIN.id
#netherrack = bl.NETHERRACK.id
#soul_sand = bl.SOUL_SAND.id
#jack = bl.JACK.id
#stained_glass = bl.STAINED_GLASS.id
#cobblestone_wall = bl.COBBLESTONE_WALL.id
#prismarine = bl.PRISMARINE.id
#sea_lantern = bl.SEA_LANTERN.id
#hay_bale = bl.HAY_BALE.id
#coal = bl.COAL_BLOCK.id
#magma = bl.MAGMA_BLOCK.id
#redstone = bl.REDSTONE_BLOCK.id
#stained_glass_pane = bl.STAINED_GLASS_PANE.id
#slime = bl.SLIME_BLOCK.id
#carpet = bl.CARPET.id
#redstone_torch = bl.REDSTONE_TORCH.id
#piston = bl.PISTON.id
#sticky_piston = bl.STICKY_PISTON.id
#dispenser = bl.DISPENSER.id
#note = bl.NOTE_BLOCK.id
#stone_pressure_plate = bl.STONE_PRESSURE_PLATE.id
#hopper = bl.HOPPER.id
#dropper = bl.DROPPER.id
#activator_rail = bl.ACTIVATOR_RAIL.id
#powered_rail = bl.POWERED_RAIL.id
#detector_rail = bl.DETECTOR_RAIL.id
#beacon = bl.BEACON.id
#emerald = bl.EMERALD_BLOCK.id
#emerald_ore = bl.EMERALD_ORE.id
#quartz = bl.QUARTZ_BLOCK.id
#barrier = bl.BARRIER.id


def getblock(name):
    return globals()[name]


def chat(text):
    conn.send("chat.post", text)


def where(target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    return Vec3(*map(int, s.split(",")))


def move(x=0, y=0, z=0, target=player, absolute=False):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    if not absolute:
        x += pos.x
        y += pos.y
        z += pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def goto(x=0, y=0, z=0, target=player):
    # s = conn.sendReceive("entity" + ".getTile", target)
    # pos = Vec3(*map(int, s.split(",")))
    # if not absolute:
    #     x += pos.x
    #     y += pos.y
    #     z += pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def changex(x=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    x += pos.x
    y = pos.y
    z = pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def changey(y=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    x = pos.x
    y += pos.y
    z = pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def changez(z=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    x = pos.x
    y = pos.y
    z += pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def setx(x=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    y = pos.y
    z = pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def sety(y=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    x = pos.x
    z = pos.z
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def setz(z=0, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    x = pos.x
    y = pos.y
    conn.send("entity" + ".setTile", target, intFloor(x, y, z))


def sphere(block, radius=10, x=0, y=0, z=0, absolute=False, hollow=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    if not hollow:
        for xd in range(radius * -1, radius):
            for yd in range(radius * -1, radius):
                for zd in range(radius * -1, radius):
                    if xd ** 2 + yd ** 2 + zd ** 2 < radius ** 2:
                        conn.send("world.setBlock", intFloor(x + xd, y + yd, z + zd, block, block_data))
    else:
        for xd in range(radius * -1, radius):
            for yd in range(radius * -1, radius):
                for zd in range(radius * -1, radius):
                    if (xd ** 2 + yd ** 2 + zd ** 2 < radius ** 2) and (xd ** 2 + yd ** 2 + zd ** 2 > (radius ** 2 - (radius * 2))):
                        conn.send("world.setBlock", intFloor(x + xd, y + yd, z + zd, block, block_data))


def circle(block,
           radius=10,
           x=0, y=0, z=0,
           direction="vertical",
           absolute=False,
           target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    if direction == "vertical":
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        xd = 0
        yd = radius
        conn.send("world.setBlock", intFloor(x, y + radius, z, block, block_data))
        conn.send("world.setBlock", intFloor(x, y - radius, z, block, block_data))
        conn.send("world.setBlock", intFloor(x + radius, y, z, block, block_data))
        conn.send("world.setBlock", intFloor(x - radius, y, z, block, block_data))
        while xd < yd:
            if f >= 0:
                yd -= 1
                ddf_y += 2
                f += ddf_y
            xd += 1
            ddf_x += 2
            f += ddf_x
            conn.send("world.setBlock", intFloor(x + xd, y + yd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x - xd, y + yd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x + xd, y - yd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x - xd, y - yd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x + yd, y + xd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x - yd, y + xd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x + yd, y - xd, z, block, block_data))
            conn.send("world.setBlock", intFloor(x - yd, y - xd, z, block, block_data))
    elif direction == "horizontal":
        f = 1 - radius
        ddf_x = 1
        ddf_z = -2 * radius
        xd = 0
        zd = radius
        conn.send("world.setBlock", intFloor(x, y, z + radius, block, block_data))
        conn.send("world.setBlock", intFloor(x, y, z - radius, block, block_data))
        conn.send("world.setBlock", intFloor(x + radius, y, z, block, block_data))
        conn.send("world.setBlock", intFloor(x - radius, y, z, block, block_data))
        while xd < zd:
            if f >= 0:
                zd -= 1
                ddf_z += 2
                f += ddf_z
            xd += 1
            ddf_x += 2
            f += ddf_x
            conn.send("world.setBlock", intFloor(x + xd, y, z + zd, block, block_data))
            conn.send("world.setBlock", intFloor(x - xd, y, z + zd, block, block_data))
            conn.send("world.setBlock", intFloor(x + xd, y, z - zd, block, block_data))
            conn.send("world.setBlock", intFloor(x - xd, y, z - zd, block, block_data))
            conn.send("world.setBlock", intFloor(x + zd, y, z + xd, block, block_data))
            conn.send("world.setBlock", intFloor(x - zd, y, z + xd, block, block_data))
            conn.send("world.setBlock", intFloor(x + zd, y, z - xd, block, block_data))
            conn.send("world.setBlock", intFloor(x - zd, y, z - xd, block, block_data))


def line(block, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0, absolute=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x1 += pos.x
        y1 += pos.y
        z1 += pos.z
        x2 = pos.x + x2
        y2 = pos.y + y2
        z2 = pos.z + z2
    # List for vertices
    vertices = []
    # If the 2 points are the same, return single vertice
    if x1 == x2 and y1 == y2 and z1 == z2:
        vertices.append(Vec3(x1, y1, z1))
    # Else get all points in edge
    else:
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        ax = abs(dx) << 1
        ay = abs(dy) << 1
        az = abs(dz) << 1
        sx = ZSGN(dx)
        sy = ZSGN(dy)
        sz = ZSGN(dz)
        x = x1
        y = y1
        z = z1
        # X dominant
        if ax >= MAX(ay, az):
            yd = ay - (ax >> 1)
            zd = az - (ax >> 1)
            loop = True
            while loop:
                vertices.append(Vec3(x, y, z))
                if x == x2:
                    loop = False
                if yd >= 0:
                    y += sy
                    yd -= ax
                if zd >= 0:
                    z += sz
                    zd -= ax
                x += sx
                yd += ay
                zd += az
        # Y dominant
        elif ay >= MAX(ax, az):
            xd = ax - (ay >> 1)
            zd = az - (ay >> 1)
            loop = True
            while loop:
                vertices.append(Vec3(x, y, z))
                if y == y2:
                    loop = False
                if xd >= 0:
                    x += sx
                    xd -= ay
                if zd >= 0:
                    z += sz
                    zd -= ay
                y += sy
                xd += ax
                zd += az
        # Z dominant
        elif az >= MAX(ax, ay):
            xd = ax - (az >> 1)
            yd = ay - (az >> 1)
            loop = True
            while loop:
                vertices.append(Vec3(x, y, z))
                if z == z2:
                    loop = False
                if xd >= 0:
                    x += sx
                    xd -= az
                if yd >= 0:
                    y += sy
                    yd -= az
                z += sz
                xd += ax
                yd += ay
    for vertex in vertices:
        conn.send("world.setBlock", intFloor(vertex.x,
                                             vertex.y,
                                             vertex.z,
                                             block,
                                             block_data))


def block(block, x=0, y=0, z=0, absolute=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    conn.send("world.setBlock", intFloor(x, y, z, block, block_data))


def blocks(block, x1=0, y1=0, z1=0, x=0, y=0, z=0, absolute=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x1 += pos.x
        y1 += pos.y
        z1 += pos.z
        x = pos.x + x
        y = pos.y + y
        z = pos.z + z
    conn.send("world.setBlocks", intFloor(x1, y1, z1, x, y, z, block, block_data))


def cube(block, side=10, x=0, y=0, z=0, absolute=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    conn.send("world.setBlocks", intFloor(x, y, z, x + side - 1, y + side - 1, z + side - 1, block, block_data))


def pyramid(block, width=11, x=0, y=0, z=0, absolute=False, target=player):
    if block is list:
        block_data = block[1]
        block = block[0]
    else:
        block_data = 0
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    if width % 2 == 0:
        width += 1
    if width == 1:
        conn.send("world.setBlock", intFloor(x, y, z, block, block_data))
    else:
        conn.send("world.setBlocks", intFloor(x, y, z, x + width - 1, y, z + width - 1, block, block_data))
        pyramid(block, width - 2, x + 1, y + 1, z + 1, absolute=True)


def over(block, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    material = int(conn.sendReceive("world.getBlock", intFloor(pos.x, pos.y - 1, pos.z)))
    if material == block:
        return True
    else:
        return False


def under(target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    material = int(conn.sendReceive("world.getBlock", intFloor(pos.x, pos.y - 1, pos.z)))
    return material


def what(x, y, z, absolute=False, target=player):
    if not absolute:
        s = conn.sendReceive("entity" + ".getTile", target)
        pos = Vec3(*map(int, s.split(",")))
        x += pos.x
        y += pos.y
        z += pos.z
    material = int(conn.sendReceive("world.getBlock", intFloor(x, y, z)))
    return material


def near(block, radius=10, target=player):
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    blocks = conn.sendReceive("world.getBlocks", intFloor(pos.x - radius,
                                                          pos.y - radius,
                                                          pos.z - radius,
                                                          pos.x + radius,
                                                          pos.y + radius,
                                                          pos.z + radius))
    blocks = map(int, blocks.split(","))
    for b in blocks:
        if b == block:
            return True
    return False


def readnumber(text=""):
    done = False
    value = 0
    while not done:
        try:
            value = int(input_from_chat(text))
            done = True
        except:
            chat("Il valore inserito non e' un numero valido")
    return value


def readstring(text=""):
    done = False
    value = 0
    while not done:
        try:
            value = input_from_chat(text)
            done = True
        except:
            chat("Il valore inserito non e' valido")
    return value


def input_from_chat(text):
    chat(text)
    read_done = False
    value = "0"
    while not read_done:
        s = conn.sendReceive("events.chat.posts")
        events = [e for e in s.split("|") if e]
        poll = [ChatEvent.Post(int(e[:e.find(",")]), e[e.find(",") + 1:]) for e in events]
        for msg in poll:
            value = msg.message
            read_done = True
            break
        time.sleep(0.10)
    return value


def polygon(block, shape=6, side=10, x=0, y=0, z=0, direction="horizontal", absolute=False, target=player):
    if direction == "horizontal":
        if block is list:
            block_data = block[1]
            block = block[0]
        else:
            block_data = 0
        if not absolute:
            s = conn.sendReceive("entity" + ".getTile", target)
            pos = Vec3(*map(int, s.split(",")))
            x = x + pos.x
            y = y + pos.y
            z = z + pos.z
        angle = 0
        i = shape
        side -= 1
        startx = x
        startz = z
        while i > 0:
            if i == 1:
                targetx = startx
                targetz = startz
            else:
                targetx = int(round(x + side * math.cos(angle), 0))
                targetz = int(round(z + side * math.sin(angle), 0))
            # Line starts here:
            # List for vertices
            vertices = []
            # If the 2 points are the same, return single vertice
            if x == targetx and y == y and z == targetz:
                vertices.append(Vec3(x, y, z))
            # Else get all points in edge
            else:
                dx = targetx - x
                dy = y - y
                dz = targetz - z
                ax = abs(dx) << 1
                ay = abs(dy) << 1
                az = abs(dz) << 1
                sx = ZSGN(dx)
                sy = ZSGN(dy)
                sz = ZSGN(dz)
                x = x
                y = y
                z = z
                # X dominant
                if ax >= MAX(ay, az):
                    yd = ay - (ax >> 1)
                    zd = az - (ax >> 1)
                    loop = True
                    while loop:
                        vertices.append(Vec3(x, y, z))
                        if x == targetx:
                            loop = False
                        if yd >= 0:
                            y += sy
                            yd -= ax
                        if zd >= 0:
                            z += sz
                            zd -= ax
                        x += sx
                        yd += ay
                        zd += az
                # Y dominant
                elif ay >= MAX(ax, az):
                    xd = ax - (ay >> 1)
                    zd = az - (ay >> 1)
                    loop = True
                    while loop:
                        vertices.append(Vec3(x, y, z))
                        if y == y:
                            loop = False
                        if xd >= 0:
                            x += sx
                            xd -= ay
                        if zd >= 0:
                            z += sz
                            zd -= ay
                        y += sy
                        xd += ax
                        zd += az
                # Z dominant
                elif az >= MAX(ax, ay):
                    xd = ax - (az >> 1)
                    yd = ay - (az >> 1)
                    loop = True
                    while loop:
                        vertices.append(Vec3(x, y, z))
                        if z == targetz:
                            loop = False
                        if xd >= 0:
                            x += sx
                            xd -= az
                        if yd >= 0:
                            y += sy
                            yd -= az
                        z += sz
                        xd += ax
                        yd += ay
            for vertex in vertices:
                conn.send("world.setBlock", intFloor(vertex.x,
                                                     vertex.y,
                                                     vertex.z,
                                                     block,
                                                     block_data))
            # line(block, x, y, z, targetx, y, targetz)
            angle += 2 * math.pi / shape
            x = targetx
            z = targetz
            i -= 1


def turtle(penblock, target=player):
    chat('Remember that class names should be Capital Letter (Turtle, not turtle)!')
    return Turtle(penblock, target)


def maze(csvpath, base=grass, wall=gold, obstacle=lava, target=player):
    # open maze csv
    f = open(csvpath, "r")
    # find player position
    s = conn.sendReceive("entity" + ".getTile", target)
    pos = Vec3(*map(int, s.split(",")))
    # define z start coordinate
    z = pos.z+1
    # for each line of the csv...
    for line in f.readlines():
        data = line.split(",")
        # restart from the original x at every loop cycle
        x = pos.x+1
        # for each cell in the list...
        for cell in data:
            if cell == "0":
                selectedblock = air
            elif cell == "2":
                selectedblock = obstacle
            else:
                selectedblock = wall
            # set the selected block
            conn.send("world.setBlock", intFloor(x, pos.y, z, selectedblock))
            conn.send("world.setBlock", intFloor(x, pos.y+1, z, selectedblock))
            # build the floor
            conn.send("world.setBlock", intFloor(x, pos.y-1, z, base))
            # move on the x axis
            x = x + 1
        # move on the z axis
        z = z + 1


#class chatListener:
    #
    #
    #def __init__(self):
        #self.start()
    #
    #def start(self) :
        #self.run = True
        #self.thread = threading.Thread(target=self.listen)
        #self.thread.start()
        #
    #def listen(self) :
        #while self.run:
            #for msg  in mc.events.pollChatPosts():
                #mc.postToChat(msg.message)
            #time.sleep(0.10)
            #
    #def exit(self) :
        #self.run = False
    #
#chatl = chatListener()


# TURTLE CLASS
class Turtle:

    SPEEDTIMES = {0: 0,
                  12: 0.001,
                  11: 0.01,
                  10: 0.1,
                  9: 0.2,
                  8: 0.3,
                  7: 0.4,
                  6: 0.5,
                  5: 0.6,
                  4: 0.7,
                  3: 0.8,
                  2: 0.9,
                  1: 1}

    def __init__(self, penblock, target=player):
        # Player
        self.player = player
        # Start position
        s = conn.sendReceive("entity" + ".getTile", target)
        self.startposition = Vec3(*map(int, s.split(",")))
        # Set turtle position
        self.position = Vec3(*map(int, s.split(",")))
        # Set turtle angles
        self.heading = 0
        self.verticalheading = 0
        # Set pen down
        self._pendown = True
        # Set pen bl to black wool
        self._penblock = bl.Block(bl.WOOL.id, 15)
        # Flying to true
        self.flying = True
        # Set speed
        self.turtlespeed = 6
        # Create turtle
        self.showturtle = True
        # Set turtle block
        self.turtleblock = bl.Block(bl.DIAMOND_BLOCK.id)
        # Draw turtle
        self.draw_turtle(int(self.position.x), int(self.position.y), int(self.position.y))
        # Previous vertical heading
        self.previous = 0
        # Last turtle
        self.last_drawn_turtle = Vec3(0, 0, 0)
        # Pen block
        self.penblock(penblock)
        # Speed
        self.speed(10)

    def forward(self, distance):
        # Get end of line
        x, y, z = self.find_point_on_sphere(self.position.x,
                                            self.position.y,
                                            self.position.z,
                                            self.heading,
                                            self.verticalheading,
                                            distance)
        # Move turtle forward
        self.move_turtle(x, y, z)

    def backward(self, distance):
        # Get end of line
        x, y, z = self.find_point_on_sphere(self.position.x,
                                            self.position.y,
                                            self.position.z,
                                            self.heading,
                                            self.verticalheading - 180,
                                            distance)
        # Move turtle forward
        self.move_turtle(x, y, z)

    def move_turtle(self, x, y, z):
        # Get blocks between current position and next
        target_x, target_y, target_z = int(x), int(y), int(z)
        # If walking, set target Y to be height of world
        if self.flying is False:
            target_y = int(conn.sendReceive(target_x, target_z))
        current_x, current_y, current_z = int(self.position.x), int(self.position.y), int(self.position.z)
        # Clear the turtle
        if self.showturtle:
            self.clear_turtle(self.last_drawn_turtle.x, self.last_drawn_turtle.y, self.last_drawn_turtle.z)
        # If speed is 0 and flying, just draw the line, else animate it
        if self.turtlespeed == 0 and self.flying:
            # Draw the line
            if self._pendown:
                line(self._penblock.id, current_x, current_y - 1, current_z, target_x, target_y - 1, target_z)
        else:
            blocks_between = getLine(current_x, current_y, current_z, target_x, target_y, target_z)
            if 215 < self.verticalheading < 315:
                self.previous = -1
                for block_between in blocks_between:
                    # If walking update the y, to be the height of the world
                    if self.flying is False:
                        block_between.y = int(conn.sendReceive(block_between.x, block_between.z))
                    # Draw the turtle
                    if self.showturtle:
                        self.draw_turtle(block_between.x, block_between.y - 2, block_between.z)
                    # Draw the pen
                    if self._pendown:
                        conn.send("world.setBlock", intFloor(block_between.x,
                                                             block_between.y - 1,
                                                             block_between.z,
                                                             self._penblock.id,
                                                             self._penblock.data))
                    # Wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    # Clear the turtle
                    if self.showturtle:
                        self.clear_turtle(block_between.x, block_between.y - 2, block_between.z)
                # Update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x, y, z
                # Draw turtle
                if self.showturtle:
                    self.draw_turtle(target_x, target_y - 2, target_z)
            elif 45 < self.verticalheading < 135:
                self.previous = 1
                for block_between in blocks_between:
                    # If walking update the y, to be the height of the world
                    if self.flying is False:
                        block_between.y = int(conn.sendReceive(block_between.x, block_between.z))
                    # Draw the turtle
                    if self.showturtle:
                        self.draw_turtle(block_between.x, block_between.y, block_between.z)
                    # Draw the pen
                    if self._pendown:
                        conn.send("world.setBlock", intFloor(block_between.x,
                                                             block_between.y - 1,
                                                             block_between.z,
                                                             self._penblock.id,
                                                             self._penblock.data))
                    # Wait
                    time.sleep(self.SPEEDTIMES[self.turtlespeed])
                    # Clear the turtle
                    if self.showturtle:
                        self.clear_turtle(block_between.x, block_between.y, block_between.z)
                # Update turtle's position to be the target
                self.position.x, self.position.y, self.position.z = x, y, z
                # Draw turtle
                if self.showturtle:
                    self.draw_turtle(target_x, target_y, target_z)
            else:
                if self.previous == -1:
                    for block_between in blocks_between:
                        # If walking update the y, to be the height of the world
                        if self.flying is False:
                            block_between.y = int(conn.sendReceive(block_between.x, block_between.z))
                        # Draw the turtle
                        if self.showturtle:
                            self.draw_turtle(block_between.x, block_between.y - 2, block_between.z)
                        if self._pendown:
                            conn.send("world.setBlock", intFloor(block_between.x,
                                                                 block_between.y - 1,
                                                                 block_between.z,
                                                                 self._penblock.id,
                                                                 self._penblock.data))
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle:
                            self.clear_turtle(block_between.x, block_between.y - 2, block_between.z)
                    # Update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x, y, z
                    # Draw turtle
                    if self.showturtle:
                        self.draw_turtle(target_x, target_y - 2, target_z)
                else:
                    for block_between in blocks_between:
                        # If walking update the y, to be the height of the world
                        if self.flying is False:
                            block_between.y = int(conn.sendReceive(block_between.x, block_between.z))
                        # Draw the turtle
                        if self.showturtle:
                            self.draw_turtle(block_between.x, block_between.y, block_between.z)
                        if self._pendown:
                            conn.send("world.setBlock", intFloor(block_between.x,
                                                                 block_between.y - 1,
                                                                 block_between.z,
                                                                 self._penblock.id,
                                                                 self._penblock.data))
                        time.sleep(self.SPEEDTIMES[self.turtlespeed])
                        if self.showturtle:
                            self.clear_turtle(block_between.x, block_between.y, block_between.z)
                    # Update turtle's position to be the target
                    self.position.x, self.position.y, self.position.z = x, y, z
                    # Draw turtle
                    if self.showturtle:
                        self.draw_turtle(target_x, target_y, target_z)
                self.previous = 0

    def right(self, angle):
        # Rotate turtle angle to the right
        self.heading = self.heading + angle
        if self.heading > 360:
            self.heading = self.heading - 360

    def left(self, angle):
        # Rotate turtle angle to the left
        self.heading = self.heading - angle
        if self.heading < 0:
            self.heading = self.heading + 360

    def up(self, angle):
        # Rotate turtle angle up
        self.verticalheading = self.verticalheading + angle
        if self.verticalheading > 360:
            self.verticalheading = self.verticalheading - 360
        # Turn flying on
        if self.flying is False:
            self.flying = True

    def down(self, angle):
        # Rotate turtle angle down
        self.verticalheading = self.verticalheading - angle
        if self.verticalheading < 0:
            self.verticalheading = self.verticalheading + 360
        # Turn flying on
        if self.flying is False:
            self.flying = True

    def goto(self, x=0, y=0, z=0, absolute=True):
        if not absolute:
            pos = where(player)
            # Clear the turtle
            if self.showturtle:
                self.clear_turtle(self.position.x,
                                  self.position.y,
                                  self.position.z)
            # Update the position
            self.position.x = pos.x + x
            self.position.y = pos.y + y
            self.position.z = pos.z + z
            # Draw the turtle
            if self.showturtle:
                self.draw_turtle(self.position.x,
                                 self.position.y,
                                 self.position.z)
        else:
            # Clear the turtle
            if self.showturtle:
                self.clear_turtle(self.position.x,
                                  self.position.y,
                                  self.position.z)
            # Update the position
            self.position.x = x
            self.position.y = y
            self.position.z = z
            # Draw the turtle
            if self.showturtle:
                self.draw_turtle(self.position.x,
                                 self.position.y,
                                 self.position.z)

    def setposition(self, x=0, y=0, z=0, absolute=False):
        self.goto(x, y, z, absolute)

    def move(self, x=0, y=0, z=0, absolute=False):
        self.goto(x, y, z, absolute)

    def setx(self, x):
        self.goto(x, self.position.y, self.position.z)

    def sety(self, y):
        self.goto(self.position.x, y, self.position.z)

    def setz(self, z):
        self.goto(self.position.x, self.position.y, z)

    def changex(self, x):
        self.move(x, 0, 0)

    def changey(self, y):
        self.move(0, y, 0)

    def changez(self, z):
        self.move(0, 0, z)

    def setheading(self, angle):
        self.heading = angle

    def setverticalheading(self, angle):
        self.verticalheading = angle
        # Turn flying on
        if self.flying is False:
            self.flying = True

    def gohome(self):
        self.goto(self.startposition.x,
                  self.startposition.y,
                  self.startposition.z)

    def pendown(self):
        self._pendown = True

    def penup(self):
        self._pendown = False

    def isdown(self):
        return self.pendown

    def fly(self):
        self.flying = True

    def walk(self):
        self.flying = False
        self.verticalheading = 0

    def penblock(self, blockId, blockData=0):
        self._penblock = bl.Block(blockId, blockData)

    def speed(self, turtlespeed):
        self.turtlespeed = turtlespeed

    def draw_turtle(self, x, y, z):
        # Draw turtle
        conn.send("world.setBlock", intFloor(x, y, z, self.turtleblock.id, self.turtleblock.data))
        self.last_drawn_turtle = Vec3(x, y, z)

    def clear_turtle(self, x, y, z):
        # Clear turtle
        conn.send("world.setBlock", intFloor(x, y, z, bl.AIR.id))

    def find_target_block(self, turtle_x, turtle_y, turtle_z, heading, verticalheading, distance):
        x, y, z = self.find_point_on_sphere(turtle_x, turtle_y, turtle_z, heading, verticalheading, distance)
        x = int(round(x, 0))
        y = int(round(y, 0))
        z = int(round(z, 0))
        return x, y, z

    def find_point_on_sphere(self, cx, cy, cz, horizontal_angle, vertical_angle, radius):
        x = cx + (radius * (math.cos(math.radians(vertical_angle)) * math.cos(math.radians(horizontal_angle))))
        y = cy + (radius * (math.sin(math.radians(vertical_angle))))
        z = cz + (radius * (math.cos(math.radians(vertical_angle)) * math.sin(math.radians(horizontal_angle))))
        return x, y, z

    def round_xyz(self, x, y, z):
        return int(round(x, 0)), int(round(y, 0)), int(round(z, 0))

    def round_vec3(self, position):
        return Vec3(int(position.x), int(position.y), int(position.z))
