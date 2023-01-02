import sys, itertools, functools, math

def compare(left, right):
    match left, right:
        case int(), int(): return left - right
        case int(), list(): return compare([left], right)
        case list(), int(): return compare(left, [right])
        case list(), list():
            for x in itertools.starmap(compare, zip(left, right)):
                if x: return x
            return len(left) - len(right)

packets = [list(map(eval, x.split("\n"))) for x in sys.stdin.read().split('\n\n')]
print(sum(i for i, x in enumerate(packets, 1) if compare(x[0], x[1]) < 0))

packets = [y for x in packets for y in x]
print((len(list(x for x in packets if compare(x, [[2]]) < 0)) + 1) * (len(list(x for x in packets if compare(x, [[6]]) < 0)) + 2))