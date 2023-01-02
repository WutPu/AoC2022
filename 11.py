import sys
import math
from copy import deepcopy
from collections import defaultdict

allData = sys.stdin.read().split('\n')

inspects = [0] * 8
items = []
ops = ["*13", "+3", "+6", "+2", "**2", "+4", "*7", "+7"]
#ops = ["*19", "+6", "**2", "+3"]
tests = []
trues = []
falses = []

for i in range(0, len(allData), 7):
    id = allData[i]
    held = allData[i + 1]
    held = [int(x) for x in held[18:].split(",")]
    items.append(held)
    op = allData[i + 2]
    test = allData[i + 3]
    test = int(test[21:])
    tests.append(test)
    true = allData[i + 4]
    true = int(true[-1])
    trues.append(true)
    false = allData[i + 5]
    false = int(false[-1])
    falses.append(false)


run = 1
for t in tests:
    print(t)
    run *= t
print(run)

for x in range(10000):
    #print(x)
    for i, monkey in enumerate(items):
        for ele in monkey:
            inspects[i] += 1
            newlvl = eval(str(ele) + ops[i])
            #newlvl = newlvl // 3
            newlvl = newlvl % run
            if (newlvl % tests[i] == 0):
                items[trues[i]].append(newlvl)
            else:
                items[falses[i]].append(newlvl)
        items[i] = []

print(items)
print(inspects)
print(sorted(inspects)[-2:])
