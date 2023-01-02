import sys, itertools, functools, math, re, sympy
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

grid = {}
instructions = ""

for r in range(len(allData)):
    line = allData[r]
    if (r != len(allData) - 1):
        for c in range(len(line)):
            if (line[c] != " "):
                grid[(r + 1) + (c + 1) * 1j] = line[c]
    else:
        instructions = line

direction = 0 + 1j

coord = 1 + 1j

while(True):
    if (coord in grid):
        if (grid[coord] == "."):
            break
    coord += 1j
pointer = 0
while(pointer < len(instructions)):
    print(int(coord.real), int(coord.imag))
    if (instructions[pointer] == "R"):
        direction *= -1j
        pointer += 1
    elif (instructions[pointer] == "L"):
        direction *= 1j
        pointer += 1
    else:
        #print(direction, coord)
        try:
            num = int(instructions[pointer:pointer + 2])
            pointer += 2
        except:
            num = int(instructions[pointer])
            pointer += 1
        for _ in range(num):
            prev = coord
            oldd = direction
            coord += direction
            #print(coord, prev, direction)
            if (coord not in grid):
                # AB
                # C
                #DF
                #E
                if (prev.real >= 1 and prev.real <= 50):
                    if (prev.imag >= 51 and prev.imag <= 100):
                        #BLOCK A
                        if (direction == 0 - 1j):
                            coord = (151 - prev.real) + (1 * 1j)
                            direction = 0 + 1j
                        elif (direction == -1 + 0j):
                            coord = ((prev.imag - 50) + 150) + (1 * 1j)
                            direction = 0 + 1j
                    elif (prev.imag >= 101 and prev.imag <= 150):
                        #BLOCK B
                        if (direction == 1 + 0j):
                            coord = (50 + (prev.imag - 100)) + (100 * 1j)
                            direction = 0 - 1j
                        elif (direction == 0 + 1j):
                            coord = (151 - prev.real) + (100 * 1j)
                            direction = 0 - 1j
                        elif (direction == -1 + 0j):
                            coord = (200) + ((prev.imag - 100) * 1j)
                            direction = -1 + 0j
                elif (prev.real >= 51 and prev.real <= 100):
                    #BLOCK C
                    if (direction == 0 - 1j):
                        coord = (101) + ((prev.real - 50) * 1j)
                        direction = 1 + 0j
                    elif (direction == 0 + 1j):
                        coord = (50) + (((prev.real - 50) + 100) * 1j)
                        direction = -1 + 0j
                elif (prev.real >= 101 and prev.real <= 150):
                    if (prev.imag >= 1 and prev.imag <= 50):
                        #BLOCK D
                        if (direction == -1 + 0j):
                            coord = (50 + (prev.imag)) + (51 * 1j)
                            direction = 0 + 1j
                        elif (direction == 0 - 1j):
                            coord = (51 - (prev.real - 100)) + (51 * 1j)
                            direction = 0 + 1j
                    elif (prev.imag >= 51 and prev.imag <= 100):
                        #BLOCK F
                        if (direction == 0 + 1j):
                            coord = (51 - (prev.real - 100)) + (150 * 1j)
                            direction = 0 - 1j
                        elif (direction == 1 + 0j):
                            coord = (150 + (prev.imag - 50)) + (50 * 1j)
                            direction = 0 - 1j
                elif (prev.real >= 151 and prev.real <= 200):
                    #BLOCK E
                    if (direction == 0 - 1j):
                        coord = (1) + (((prev.real - 150) + 50) * 1j)
                        direction = 1 + 0j
                    elif (direction == 1 + 0j):
                        coord = (1) + ((prev.imag + 100) * 1j)
                        direction = 1 + 0j
                    elif (direction == 0 + 1j):
                        coord = (150) + (((prev.real - 150) + 50) * 1j)
                        direction = -1 + 0j
                #print("wrap:", coord, direction, ", old:", prev, oldd)
            if (grid[coord] == "#"):
                coord = prev
                direction = oldd
                break
            
value = {
    1 + 0j: 1,
    -1 + 0j: 3,
    0 - 1j: 2,
    0 + 1j: 0
}


print(coord, direction)
print(int(1000 * coord.real + 4 * coord.imag + value[direction]))