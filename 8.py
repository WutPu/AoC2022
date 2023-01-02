import sys
import math
from copy import deepcopy
from collections import defaultdict

allData = sys.stdin.read().split('\n')

grid = []

max_tile = [0, 0]
max_score = 0

for i in range(len(allData)):
    line = allData[i]
    grid.append([int(x) for x in list(line)])

for r in range(len(grid)):
    for c in range(len(grid[r])):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        score = 1
        for d, d2 in dirs:
            dr, dc = r, c
            sum = 0
            max = grid[r][c]
            while(True):
                dr, dc = dr + d, dc + d2
                if(dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[r]) and max > grid[dr][dc]):  
                    sum += 1
                else:
                    if(dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[r])):
                        sum += 1
                    break
            score *= sum
        if (score > max_score):
            max_score = score
            max_tile = [r, c]

print(max_score)
