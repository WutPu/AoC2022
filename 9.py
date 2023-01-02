import sys
import math
from copy import deepcopy
from collections import defaultdict

allData = sys.stdin.read().split('\n')

points = []
c = [0, 0]
p = [[0, 0]]

q = {
    "U": [0, -1],
    "D": [0, 1],
    "L": [-1, 0],
    "R": [1, 0]
}


for i in range(len(allData)):
    line = allData[i]
    d, a = line.split(" ")
    a = int(a)
    for x in range(a):
        c = [c[0] + q[d][0], c[1] + q[d][1]]
        t = p[-1]
        for i in range(len(p)):
            cur = p[len(p) - 1 - i][:]
            if (i == 0):
                compare = c[:]
            else:
                compare = p[len(p) - i][:]
            if (math.sqrt((cur[0] - compare[0]) ** 2 + (cur[1] - compare[1]) ** 2) > math.sqrt(2)):
                if (cur[0] > compare[0]):
                    cur[0] -= 1
                elif (cur[0] < compare[0]):
                    cur[0] += 1
                if (cur[1] > compare[1]):
                    cur[1] -= 1
                elif (cur[1] < compare[1]):
                    cur[1] += 1  
            p[len(p) - 1 - i] = cur[:]
        if (len(p) < 9 and p[0] != [0, 0]):
            p.insert(0, [0, 0])
        if (p[0] not in points):
            points.append(p[0])
    '''grid = []
    for row in range(30):
        r = []
        for cell in range(30):
            if ([cell - 15, row - 15] in p):
                r.append(str(p.index([cell - 15, row - 15])))
            elif([cell - 15, row - 15] == c):
                r.append("H")
            else:
                r.append(".")
        grid.append(r)

    for r in grid:
        print("".join(r))
    print(points)'''



print(points)
print(len(points))