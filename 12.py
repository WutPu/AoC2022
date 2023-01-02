import sys
import math
from copy import deepcopy
from collections import defaultdict

allData = sys.stdin.read().split('\n')

grid = []
for i in range(0, len(allData)):
    line = allData[i]
    grid.append(list(line))

end = [0, 0]
start = [0, 0]
queue = []

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if (cell == "S" or cell == "a"):
            #start = [i, j]
            queue.append([i, j])
        if (cell == "E"):
            end = [i, j]

cache = {",".join([str(x) for x in start]) : 0}

#queue = [start]
time = 1
print(queue)
while(end not in queue):
    nqueue = []
    if (queue != []):
        print(queue)
    for posr, posc in queue:
        new = [[posr + 1, posc], [posr - 1, posc], [posr, posc + 1], [posr, posc - 1]]
        if (grid[posr][posc] == "S"):
            ele = 100
        else:
            ele = ord(grid[posr][posc])
        for newposr, newposc in new:
            if (newposr > 0 and newposr < len(grid) and newposc > 0 and newposc < len(grid[0])):
                if (ord(grid[newposr][newposc]) <= ele + 1 or grid[newposr][newposc] == "E"):
                    if (",".join([str(x) for x in [newposr, newposc]]) not in cache):
                        cache[",".join([str(x) for x in [newposr, newposc]])] = time
                        nqueue.append([newposr, newposc])
                    else:
                        if (cache[",".join([str(x) for x in [newposr, newposc]])] > time):
                            cache[",".join([str(x) for x in [newposr, newposc]])] = time
                            nqueue.append([newposr, newposc])
    time += 1
    queue = deepcopy(nqueue)
print(cache[",".join([str(x) for x in end])])