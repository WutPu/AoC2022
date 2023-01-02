import sys
import math
from copy import deepcopy
from collections import defaultdict

allData = sys.stdin.read().split('\n')

a = defaultdict(list)

prev = []
current = "/"

for i in range(len(allData)):
    line = allData[i]
    if (line[0] == "$"):
        try:
            cmd, d = line[2:].split(" ")
            print(current)
            if (d == ".."):
                current = prev[-1]
                del prev[-1]
            elif (d == "/"):
                prev = []
                current = "/"
            else:
                prev.append(current)
                current = d
        except:
            q = i + 1
            while (allData[q][0] != "$"):
                c, f = allData[q].split(" ")
                try:
                    c = int(c)
                    a["_".join(prev + [current])].append(c)
                except:
                    a["_".join(prev + [current])].append("_".join(prev + [current, f]))
                q += 1
                if(q >= len(allData)):
                    break
sys.setrecursionlimit(100000)
print(dict(a))

cache = {}
def s(a, k):
    global cache
    l = a[k]
    #print(k)
    for i in range(len(l)):
        if (type(l[i]) != int):
            if (l[i] in cache):
                l[i] = cache[l[i]]
            else:
                q = s(a, l[i])
                cache[l[i]] = q
                l[i] = q
    return sum(l)

score = []

for k in list(a):
    q = s(a, k)
    if(q):
        score.append(q)
print(score)

min = math.inf
for i in range(len(score)):
    a = 44359867 - score[i]
    if (a <= 40000000):
        if (score[i] < min):
            min = score[i]

print(min)