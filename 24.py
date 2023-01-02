import sys, itertools, functools, math, re, sympy
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

grid = {}
blizzards = []

directions = {
    ">": 0 + 1j,
    "<": 0 - 1j,
    "v": 1 + 0j,
    "^": -1 + 0j
}

for r in range(len(allData)):
    line = allData[r]
    for c in range(len(line)):
        if (line[c] in directions):
            blizzards.append([r + c * 1j, line[c]])
            grid[r + c * 1j] = "."
        else:
            grid[r + c * 1j] = line[c]

start = 0 + 1j
end = 21 + 150j

queue = deque([start])

options = [0 + 1j, 0 - 1j, 1 + 0j, -1 + 0j, 0 + 0j]
visited = {start: 0}
visits = 0

timer = 0
while (visits <= 2):
    print(len(queue), timer, end='\r', flush=True)
    if (end in queue and visits == 0):
        print("PART 1:", timer)
        visits += 1
        visited = {end: timer}
        queue = deque([end])
    if (start in queue and visits == 1):
        visits += 1
        visited = {start: timer}
        queue = deque([start])
    if (end in queue and visits == 2):
        visits += 1
        print("PART 2:", timer)
    for i in range(len(blizzards)):
        pos, dir = blizzards[i]
        if (grid[directions[dir] + pos] != "#"):
            blizzards[i] = [directions[dir] + pos, dir]
        else:
            if (dir == ">"):
                blizzards[i] = [pos.real + 1j, dir]
            elif (dir == "<"):
                blizzards[i] = [pos.real + 150j, dir]
            elif (dir == "^"):
                blizzards[i] = [20 + pos.imag * 1j, dir]
            elif (dir == "v"):
                blizzards[i] = [1 + pos.imag * 1j, dir]
    for _ in range(len(queue)):
        state = queue.popleft()
        for dir in options:
            new = state + dir
            if (new.real >= 0.0 and new.real <= 21):
                if (grid[new] != "#"):
                    notBlizzard = True
                    for blizzard, _ in blizzards:
                        if (blizzard == new):
                            notBlizzard = False
                    if (notBlizzard):
                        if (new not in queue):
                            if (new not in visited):
                                queue.append(new)
                                visited[new] = timer
                            elif (visited[new] >= timer - 12):
                                queue.append(new)
    timer += 1