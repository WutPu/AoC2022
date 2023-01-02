import sys
import math

allData = sys.stdin.read().split('\n')
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
for x in range(0, len(allData), 3):
    a, b, c = allData[x], allData[x + 1], allData[x + 2]
    print(a, b, c)
    for letter in a:
        if letter in b and letter in c:
            print(score)
            score += s.index(letter) + 1
            break
    
print(score)