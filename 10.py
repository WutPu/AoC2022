import sys
import math

allData = sys.stdin.read().split('\n')

str = 0
x = 1
cycle = 0
grid = []
for r in range(6):
    row = []
    for c in range(40):
        row.append(".")
    grid.append(row)

for i in range(len(allData)):
    line = allData[i]
    for r in grid:
        print("".join(r))
    print(cycle // 40, cycle % 40)
    try:
        op, value = line.split(" ")
        for y in range(2):
            if ((cycle % 40) >= x - 1 and (cycle % 40) <= x + 1):
                grid[cycle // 40][cycle % 40] = "#"
            cycle += 1
        value = int(value)
        x += value
    except:
        if ((cycle % 40) >= x - 1 and (cycle % 40) <= x + 1):
            grid[cycle // 40][cycle % 40] = "#"
        cycle += 1

for r in grid:
    print("".join(r))

print(str)