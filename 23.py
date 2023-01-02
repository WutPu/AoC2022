import sys, itertools, functools, math, re, sympy
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

grid = defaultdict(lambda: '.')


for r in range(len(allData)):
    line = allData[r]
    for c in range(len(line)):
        grid[r + c * 1j] = line[c]

directions = {
    "N": -1 + 0j,
    "NE": -1 + 1j,
    "NW": -1 - 1j,
    "E": 0 + 1j,
    "S": 1 + 0j,
    "SE": 1 + 1j,
    "SW": 1 - 1j,
    "W": 0 - 1j
}

prio = [["N", "NE", "NW"], ["S", "SE", "SW"], ["W", "NW", "SW"], ["E", "NE", "SE"]]


for round in range(10000):
    nomove = True
    print(round, prio)
    rbound = (math.inf, 0)
    cbound = (math.inf, 0)
    dests = {}
    conflicts = []
    elves = []
    for elf in grid:
        if (grid[elf] == "#"):
            elves.append(elf)
    for elf in elves:
        plan = 0
        if (not (grid[directions["E"] + elf] == "." and grid[directions["NE"] + elf] == "." and grid[directions["SE"] + elf] == "." and grid[directions["N"] + elf] == "." and grid[directions["S"] + elf] == "." and grid[directions["W"] + elf] == "." and grid[directions["NW"] + elf] == "." and grid[directions["SW"] + elf] == ".")):
            for ponder in prio:
                allempty = True
                for direction in ponder:
                    if (grid[directions[direction] + elf] != "."):
                        allempty = False
                        break
                if (allempty):
                    plan = directions[ponder[0]]
                    break
            if (plan != 0):
                nomove = False
                if (plan + elf not in dests):
                    dests[plan + elf] = elf
                else:
                    conflicts.append(plan + elf)
    #print(dests, conflicts)
    for dest in dests:
        if dest not in conflicts:
            grid[dests[dest]] = "."
            grid[dest] = "#"
    prio.append(prio[0])
    del prio[0]

    if (nomove):
        print(round + 1)
        break


rbound = (math.inf, 0)
cbound = (math.inf, 0)

for k in grid:
    if (grid[k] == "#"):
        rbound = (min(rbound[0], k.real), max(rbound[1], k.real))
        cbound = (min(cbound[0], k.imag), max(cbound[1], k.imag))

print(rbound, cbound)

answer = 0

for r in range(int(rbound[0]), int(rbound[1] + 1)):
    row = []
    for c in range(int(cbound[0]), int(cbound[1] + 1)):
        row.append(grid[r + c * 1j])
        if (grid[r + c * 1j] == "."):
            answer += 1
    print("".join(row))

print(answer)
