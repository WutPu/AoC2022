import sys, itertools, functools, math
from collections import Counter, defaultdict
from copy import deepcopy

allData = sys.stdin.read().split('\n')

valves = {}


for i in range(len(allData)):
    line = allData[i]
    if ("valves" in line):
        line = line.replace("Valve ", "").replace(" has flow rate=", ";").replace(" tunnels lead to valves ", "")
    else:
        line = line.replace("Valve ", "").replace(" has flow rate=", ";").replace(" tunnel leads to valve ", "")
    print(line)
    name, rate, dests = line.split(";")
    dests = dests.split(", ")
    if (type(dests) == str):
        dests = [dests]
    valves[name] = [int(rate), dests]

most = 0
path = []
queue = [["AA", 0, 1, []]]
cache = defaultdict(lambda:-1)
while(len(queue) > 0):
    print(queue)
    newQueue = []
    for each in queue:
        name, flow, time, open = deepcopy(each)
        if (flow > most):
            most = flow
            path = open
        if (time <= 30):
            flowRate, dests = valves[name]
            for dest in dests:
                if (cache[dest] < flow):
                    newQueue.append(deepcopy([dest, flow, time + 1, open]))
                    cache[dest] = flow
            if (name not in open):
                open.append(name)
                flow += flowRate * (30 - time)
                newQueue.append(deepcopy([name, flow, time + 1, open]))
    queue = deepcopy(newQueue)

print(most, path)