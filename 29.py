l = set()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        l.add(a**b)

print len(set(l))
