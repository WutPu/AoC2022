import sys
import math

allData = sys.stdin.read().split('\n')

score = 0

for line in allData:
    a, b = line.split(",")
    a, b = [int(x) for x in a.split("-")], [int(x) for x in b.split("-")]
    if ((a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[0] <= a[1]) or (b[1] >= a[0] and b[1] <= a[1])):
        score += 1

print(score)