import sys, itertools, functools, math, re, sympy
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

nums = {}

for i in range(len(allData)):
    name, eq = allData[i].split(": ")
    nums[name] = eq

answer = 0

def value(monkey, x=0):
    if (monkey == "humn" and x != 0):
        return x
    try:
        return int(nums[monkey])
    except:
        string = nums[monkey]
        return eval(str(value(string[:4], x)) + string[5] + str(value(string[-4:], x)))

print("PART 1", int(value("root")))

match = value("vqfc")
print("MATCHING TO", int(value("vqfc")))

def value2(monkey):
    if (monkey == "humn"):
        return "x"
    if(len(nums[monkey]) < 5):
        return str(nums[monkey])
    else:
        string = nums[monkey]
        s = "(" + str(value2(string[:4])) + string[5] + str(value2(string[-4:])) + ")"
        if ("x" in s):
            return s
        else:
            return eval(s)

unknown = value2("wrvq")
eq = unknown + "=" + str(match)
sympy_eq = sympy.sympify("Eq(" + eq.replace("=", ",") + ")")
answer = sympy.solve(sympy_eq)[0]
print("PART 2", int(answer))
print("CHECK DOES THIS MATCH", int(value("wrvq", answer)) == int(match))