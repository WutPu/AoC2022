import sys, itertools, functools, math, re
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

value = 0

orecosts = []
claycosts = []
obsidiancosts = []
geodecosts = []


for i in range(len(allData)):
    print(allData[i][15:].split(".")[:-1])
    ore, clay, obsidian, geode = allData[i][15:].split(".")[:-1]
    ore = int(ore.replace("ach ore robot costs ", "").replace("ch ore robot costs ", "").replace(" ore", ""))
    clay = int(clay.replace("Each clay robot costs ", "").replace(" ore", ""))
    obsidian = obsidian.replace("Each obsidian robot costs ", "").replace("clay", "").split("ore and ")
    obsidian = int(obsidian[0]) + int(obsidian[1]) * 1j
    geode = geode.replace("Each geode robot costs ", "").replace("obsidian", "").split("ore and ")
    geode = int(geode[0]) + int(geode[1]) * 1j
    orecosts.append(ore)
    claycosts.append(clay)
    obsidiancosts.append(obsidian)
    geodecosts.append(geode)

print(orecosts, claycosts, obsidiancosts, geodecosts)

answer = 1
seen = set()

for i in range(1):
    costs = [orecosts[i], claycosts[i], obsidiancosts[i], geodecosts[i]]
    maxgeodes = 0
    queue = [(0, 0, 0, 0, 1, 0, 0, 0)]
    for minutes in range(49):
        print(len(queue), i,  minutes)
        nqueue = []
        for state in queue:
            nqueue.append((state[0] + state[4], state[1] + state[5], state[2] + state[6], state[3] + state[7], state[4], state[5], state[6], state[7]))
            if (state[0] >= costs[0]):
                nqueue.append((state[0] + state[4] - costs[0], state[1] + state[5], state[2] + state[6], state[3] + state[7], state[4] + 1, state[5], state[6], state[7]))
            if (state[0] >= costs[1]):
                nqueue.append((state[0] + state[4] - costs[1], state[1] + state[5], state[2] + state[6], state[3] + state[7], state[4], state[5] + 1, state[6], state[7]))
            if (state[0] >= int(costs[2].real) and state[1] >= int(costs[2].imag)):
                nqueue.append((state[0] + state[4] - int(costs[2].real), state[1] + state[5] - int(costs[2].imag), state[2] + state[6], state[3] + state[7], state[4], state[5], state[6] + 1, state[7]))
            if (state[0] >= int(costs[3].real) and state[2] >= int(costs[3].imag)):
                nqueue.append((state[0] + state[4] - int(costs[3].real), state[1] + state[5], state[2] + state[6] - int(costs[3].imag), state[3] + state[7], state[4], state[5], state[6], state[7] + 1))
        nqueue.sort(key=lambda x: int(x[4]))
        nqueue.sort(key=lambda x: int(x[0]))
        nqueue.sort(key=lambda x: int(x[5]))
        nqueue.sort(key=lambda x: int(x[1]))
        nqueue.sort(key=lambda x: int(x[6]))
        nqueue.sort(key=lambda x: int(x[2]))
        nqueue.sort(key=lambda x: int(x[7]))
        nqueue.sort(key=lambda x: int(x[3]))
        queue = deepcopy(nqueue[-1000:])
    print(queue)
    answer *= (queue[-1][3])

print(queue)
print(answer)