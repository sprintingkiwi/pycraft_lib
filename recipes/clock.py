from pycraft_minetest import *
import datetime
ov = 0
mv = 0
sv = 0
pos = where()
size = 10
hoursblock = wood
minutesblock = grass
secondsblock = glowstone
circle(gold, size + 2, y=-2, direction="horizontal")
circle(gold, size + 2, y=-1, direction="horizontal")
circle(gold, size + 2, direction="horizontal")

while True:
    now = datetime.datetime.now()
    o = now.hour
    m = now.minute
    s = now.second
    if ov != o:
        angle_ov = ov * 30
        line(air,
            pos.x,
            pos.y - 2,
            pos.z,
            pos.x + int(size * math.cos(math.radians(angle_ov))),
            pos.y - 2,
            pos.z + int(size * math.sin(math.radians(angle_ov))),
            absolute=True)
        angle_o = o * 30
        line(hoursblock,
            pos.x,
            pos.y - 2,
            pos.z,
            pos.x + int(size * math.cos(math.radians(angle_o))),
            pos.y - 2,
            pos.z + int(size * math.sin(math.radians(angle_o))),
            absolute=True)
        ov = o
    if mv != m:
        angle_mv = mv * 6
        line(air,
             pos.x,
             pos.y - 1,
             pos.z,
             pos.x + int(size * math.cos(math.radians(angle_mv))),
             pos.y - 1,
             pos.z + int(size * math.sin(math.radians(angle_mv))),
             absolute=True)
        angle_m = m * 6
        line(minutesblock,
            pos.x,
            pos.y - 1,
            pos.z,
            pos.x + int(size * math.cos(math.radians(angle_m))),
            pos.y - 1,
            pos.z + int(size * math.sin(math.radians(angle_m))),
            absolute=True)
        mv = m
    if sv != s:
        chat(str(o) + " : " + str(m) + " : " + str(s))
        angle_sv = sv * 6
        line(air,
            pos.x,
            pos.y,
            pos.z,
            pos.x + int(size * math.cos(math.radians(angle_sv))),
            pos.y,
            pos.z + int(size * math.sin(math.radians(angle_sv))),
            absolute=True)
        angle_s = s * 6
        line(secondsblock,
            pos.x,
            pos.y,
            pos.z,
            pos.x + int(size * math.cos(math.radians(angle_s))),
            pos.y,
            pos.z + int(size * math.sin(math.radians(angle_s))),
            absolute=True)
        sv = s
