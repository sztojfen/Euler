import math


def is_pent(num):
    test = (math.sqrt(24*num + 1) + 1) / 6
    return test == int(test)

def is_hex(num):
    test = (math.sqrt(8*num + 1) + 1) / 4
    return test == int(test)

found = False
i = 286
while not found:
    t = i * (i + 1) / 2
    if is_pent(t) and is_hex(t):
        print t
        found = True
    i += 1
