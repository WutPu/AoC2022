import sys

allData = sys.stdin.read().split('\n')

grid = {}

abyss = 0

for i in range(len(allData)):
    line = allData[i]
    line = [[int(y) for y in x.split(",")] for x in line.split(" -> ")]
    for (x1, y1), (x2, y2) in zip(line, line[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x + y * 1j] = "#"
                abyss = max(y, abyss)

num = 0
fell = []

while(500 + 0j not in grid):
    sand = 500 + 0j
    while(sand.imag < abyss + 1):
        for dest in sand + 1j, sand -1 + 1j, sand + 1 + 1j:
            if (dest not in grid):
                sand = dest
                break
        else:
            break
    if (sand.imag >= abyss - 1):
        fell.append(num)
    grid[sand] = "o"
    num += 1

print("Part 1: " + str(fell[0]))
print("Part 2: " + str(num))