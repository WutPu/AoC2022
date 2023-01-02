import sys, itertools, functools, math, re, sympy
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

numbers = {"2":2, "1":1, "0":0, "-":-1, "=":-2}

answer = 0

for r in range(len(allData)):
    line = allData[r][::-1]
    number = 0
    for i, char in enumerate(line):
        number += numbers[char] * (5 ** i)
    answer += number

print(answer)