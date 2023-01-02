import sys, itertools, functools, math
from collections import Counter, defaultdict
from copy import deepcopy

allData = sys.stdin.read().split('\n')

#PLS BE EASY I WANT TO SLEEP ok that was kinda easy ty
answer = 0

for i in range(len(allData)):
    jets = allData[i]

rocks = [
    [["#", "#", "#", "#"]],
    [[".", "#", "."],
     ["#", "#", "#"],
     [".", "#", "."]],
    [[".", ".", "#"],
     [".", ".", "#"],
     ["#", "#", "#"]],
    [["#"],
     ["#"],
     ["#"],
     ["#"]],
    [["#", "#"],
     ["#", "#"]]
]

grid = {}

height = 0
time = 0

def checkcollision(shape, grid, posx, posy):
    if (posy + len(shape) - 1 >= 0):
        for r, row in enumerate(shape):
            for c, cell in enumerate(row):
                if ((posx + c) + (posy - r) * 1j in grid and cell == "#"):
                    return False
    else:
        return False
    return True

print(len(jets))

seen = {}
heights = {}
for x in range(1000000000000):
    #if ()
    #print(x, height)
    heights[x] = height
    cur = rocks[x % 5]
    #print(height)
    rx, ry = 2, height + 3 + (len(cur) - 1)
    new = []
    while(True):
        wind = jets[time % len(jets)]
        #print(rx, ry)
        if (wind == ">"):
            if (rx < 7 - len(cur[0])):
                if (checkcollision(cur, grid, rx + 1, ry)):
                    rx += 1
        elif (wind == "<"):
            if (rx > 0):
                if (checkcollision(cur, grid, rx - 1, ry)):
                    rx -= 1
        time += 1
        if (checkcollision(cur, grid, rx, ry - 1)):
            ry -= 1
        else:
            for r, row in enumerate(cur):
                for c, cell in enumerate(row):
                    if (cell == "#"):
                        grid[(rx + c) + (ry - r) * 1j] = "#"
                        new.append((rx + c) + (ry - r) * 1j)
            break
    for k in new:
        if (k.imag + 1 > height):
            height = int(k.imag + 1)
    checksum = str(time % len(cur[0])) + "," + str(x % 5)
    for y2 in range(height, max(-1, height - 200), -1):
        r2 = []
        for x2 in range(0, 7):
            if (x2 + y2 * 1j in grid):
                r2.append("#")
            else:
                r2.append(".")
        checksum = checksum + "," "".join(r2)
    if (checksum not in seen):
        seen[checksum] = [x, height]
    else:
        print("DUMB?", seen[checksum], [x, height])
        answer = height
        cycle = x - seen[checksum][0]
        added = height - seen[checksum][1]
        hi = 1000000000000
        hi -= x
        numcycles = hi // cycle
        answer += numcycles * added
        remainder = hi - (numcycles * cycle)
        print("TEMP", answer, remainder)
        answer += (heights[seen[checksum][0] + remainder] - seen[checksum][1])
        print("ANSWER", answer, heights[seen[checksum][0] + remainder])
        break
#print(x, height)

for y in range(0 + 0, -1, -1):
    r = []
    for x in range(0, 7):
        if (x + y * 1j in grid):
            r.append("#")
        else:
            r.append(".")
    #print("".join(r))

#print(height)