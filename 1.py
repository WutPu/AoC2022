import sys
import math

allData = sys.stdin.read().split('\n')

max = []
counter = 0
for line in allData:
    if (len(line) != 0):
        counter += int(line)
    else:
        max.append(counter)
        counter = 0

max = sorted(max)
print(max)