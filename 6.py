import sys
import math

allData = sys.stdin.read().split('\n')

score = 0

marker = []
for i in range(len(allData[0])):
    print(allData[0][i:i+14])
    if(len(set(allData[0][i:i+14])) == 14):
        print(i + 1 + 13)
        break
