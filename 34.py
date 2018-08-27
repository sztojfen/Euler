def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)

fac_t = []
result = 0
for i in xrange(10):
    fac_t.append(fac(i))

for i in range(3, 100000):  # for 1 and 2 there are no sums!
    facsum = sum([fac_t[int(n)] for n in str(i)])
    if facsum == i:
        result += i

print result