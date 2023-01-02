import sys
import math

allData = sys.stdin.read().split('\n')
score = 0

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

results = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8, 
    "B X": 1,
    "B Y": 5,
    "B Z": 9, 
    "C X": 2,
    "C Y": 6,
    "C Z": 7, 
}

score = 0
for line in allData:
    score += results[line]


print(score)
