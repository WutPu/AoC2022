import sys, itertools, functools, math
from collections import Counter, defaultdict

allData = sys.stdin.read().split('\n')

sensors = set()
beacons = set()
lo = 0
hi = 0
for i in range(len(allData)):
    sensor, beacon = allData[i].split(":")
    sensor = sensor.replace("Sensor at x=", "").replace(" y=", "").split(",")
    beacon = beacon.replace(" closest beacon is at x=", "").replace(" y=", "").split(",")
    dist = abs(int(sensor[0]) - int(beacon[0])) + abs(int(sensor[1]) - int(beacon[1]))
    if (int(sensor[0]) - dist < lo):
        lo = int(sensor[0]) - dist
    if (int(sensor[0]) + dist > hi):
        hi = int(sensor[0]) + dist
    sensors.add(",".join(sensor + [str(dist)]))
    beacons.add(",".join(beacon))

print(lo, hi)

x = 0
y = 0
prevx = x
prevy = y
done = False
while(True):
    prevx = x
    prevy = y
    print(x, y)
    if (x > 4000000):
        y += 1
        x = 0
    cant = False
    for k in sensors:
        sensorx, sensory, dist = [int(z) for z in k.split(",")]
        if (abs(x - sensorx) + abs(y - sensory) <= dist):
            x = sensorx + (dist - abs(y - sensory))
            cant = True
            break
    if (cant == False and x <= 4000000 and y <= 4000000):
        print(x, y)
        print(x * 4000000 + y)
        break
    if ([x, y] == [prevx, prevy]):
        x += 1