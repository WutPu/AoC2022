import sys
import math

allData = sys.stdin.read().split('\n')

'''
"T"     "D"         "L"            
"R"     "S" "G"     "P"         "H"
"G"     "H" "W"     "R" "L"     "P"
"W"     "G" "F" "H" "S" "M"     "L"
"Q"     "V" "B" "J" "H" "N" "R" "N"
"M" "R" "R" "P" "M" "T" "H" "Q" "C"
"F" "F" "Z" "H" "S" "Z" "T" "D" "S"
"P" "H" "P" "Q" "P" "M" "P" "F" "D"
 1   2   3   4   5   6   7   8   9 
'''

grid = [
    ["P", "F", "M", "Q", "W", "G", "R", "T"],
    ["H", "F", "R"],
    ["P", "Z", "R", "V", "G", "H", "S", "D"],
    ["Q", "H", "P", "B", "F", "W", "G"],
    ["P", "S", "M", "J", "H"],
    ["M", "Z", "T", "H", "S", "R", "P", "L"],
    ["P", "T", "H", "N", "M", "L"],
    ["F", "D", "Q", "R"],
    ["D", "S", "C", "N", "L", "P", "H"]
]

del allData[0:10]
for line in allData:
    if (len(line) == 18):
        a = int(line[5])
    else:
        a = int(line[5:7])
    b = int(line[-6])
    c = int(line[-1])
    print(grid[b-1][-a:])
    for q in grid[b-1][-a:]:
        grid[c - 1].append(q)
    del grid[b - 1][-a:]
    #a -= 1

for line in grid:
    print(line[-1])