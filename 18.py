import sys, itertools, functools, math
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

cubes = []

minx, miny, minz = [math.inf, math.inf, math.inf]
maxx, maxy, maxz = [0, 0, 0]

for i in range(len(allData)):
    line = [int(x) for x in allData[i].split(",")]
    x, y, z = line
    minx, miny, minz = min(minx, x), min(miny, y), min(minz, z)
    maxx, maxy, maxz = max(maxx, x), max(maxy, y), max(maxz, z)
    cubes.append(line)

answer = 0

queue = deque()
queue.append([minx - 1, miny - 1, minz - 1])
visited = {}
while(len(queue) > 0):
    x, y, z = queue.popleft()
    print(answer, len(queue), len(visited))
    for dirx, diry, dirz in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
        #print([x + dirx, y + diry, z + dirz])
        if (x >= minx - 1 and x <= maxx + 1 and y >= miny - 1 and y <= maxy + 1 and z >= minz - 1 and z <= maxz + 1):
            if (','.join(str(q) for q in [x + dirx, y + diry, z + dirz]) not in visited):
                if ([x + dirx, y + diry, z + dirz] in cubes):
                    answer += 1
                else:
                    visited[','.join(str(q) for q in [x + dirx, y + diry, z + dirz])] = "#"
                    queue.append([x + dirx, y + diry, z + dirz])

print("YOU WIN $" + str(answer))