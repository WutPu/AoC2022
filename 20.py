import sys, itertools, functools, math, re
from collections import Counter, defaultdict, deque
from copy import deepcopy

allData = sys.stdin.read().split('\n')

nums = deque()

for i in range(len(allData)):
    line = int(allData[i])
    nums.append([line * 811589153, i])
    #line = re.findall(r'\d+', line)

for _ in range(10):
    print(_)
    for x in range(len(nums)):
        while nums[0][1] != x:
            nums.append(nums.popleft())
        element = nums.popleft()
        newidx = element[0] % len(nums)
        for _ in range(newidx):
            nums.append(nums.popleft())
        nums.append(element)

for zero in range(len(nums)):
    if (nums[zero][0] == 0):
        break

print(len(nums))
print(nums[(1000 + zero) % len(nums)][0], nums[(2000 + zero) % len(nums)][0], nums[(3000 + zero) % len(nums)][0])

print(nums[(1000 + zero) % len(nums)][0] + nums[(2000 + zero) % len(nums)][0] + nums[(3000 + zero) % len(nums)][0])