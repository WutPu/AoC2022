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
    name, rate, dests = line.split(";")
    dests = dests.split(", ")
    if (type(dests) == str):
        dests = [dests]
    valves[name] = [int(rate), dests]

most = 0
path = []
queue = [["AA", "AA", 0, 1, []]]
cache = defaultdict(lambda:-1)
time = ":p"
while(len(queue) > 0):
    print(time, len(queue), most)
    newQueue = []
    for each in queue:
        name, elephant, flow, time, open = deepcopy(each)
        if (flow > most):
            most = flow
            path = open
        if (time <= 26):
            flowRate, dests = valves[name]
            flowRate2, dests2 = valves[elephant]
            for dest in dests:
                for dest2 in dests2:
                    newQueue.append(deepcopy([dest, dest2, flow, time + 1, open]))
            if (flowRate != 0):
                for dest2 in dests2:
                    if (name not in open):
                        newQueue.append(deepcopy([name, dest2, flow + flowRate * (26 - time), time + 1, open + [name]]))
            if (flowRate2 != 0):
                for dest in dests:
                    if (elephant not in open):
                        newQueue.append(deepcopy([dest, elephant, flow + flowRate2 * (26 - time), time + 1, open + [elephant]]))
            if (flowRate != 0 and flowRate2 != 0 and name != elephant):
                if (name not in open and elephant not in open):
                    newQueue.append(deepcopy([name, elephant, flow + flowRate * (26 - time) + flowRate2 * (26 - time), time + 1, open + [name, elephant]]))
    newQueue.sort(key=lambda x: int(x[2]))
    queue = deepcopy(newQueue[-10000:])

print(most, path)