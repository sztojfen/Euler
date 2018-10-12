import scipy.special

counter = 0
for i in xrange(23, 101):
    print i
    for j in range(i):
        if scipy.special.binom(i, j) > 1000000:
            counter += 1

print counter