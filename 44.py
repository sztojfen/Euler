import math


def is_pent(num):
    test = (math.sqrt(24*num +1) + 1) / 6
    return test == int(test)

found = False
i = 1
while not found:
    m = i * (3 * i - 1) / 2
    for j in range(i, 0, -1):
        n = j*(3*j-1)/2
        print m,n
        if is_pent(m+n) and is_pent(m-n):
            print m-n
            found = True
            break
    i += 1
