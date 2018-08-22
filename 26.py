num = longest = 1

for d in xrange(3,10,2):
    if d % 5 == 0:
        continue

    p = 1
    while (10 ** p) % d != 1:
        p += 1

    if p > longest:
        num, longest = d, p

print num, longest