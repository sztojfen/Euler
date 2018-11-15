def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

result = 0
for a in xrange(1, 100):
    print a
    for b in xrange(1, 100):
        if sum_digits3(a**b) > result:
            result = sum_digits3(a**b)

print result