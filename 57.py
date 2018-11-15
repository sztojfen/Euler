def length(x):
    return len(str(x))

nominators = [1] + [3] + [0]*999
denominators = [1] + [2] + [0]*999
for i in xrange(2, 1001):
    nominators[i] = 2 * nominators[i - 1] + nominators[i - 2]
    denominators[i] = 2 * denominators[i - 1] + denominators[i - 2]

n_lengths = map(length, nominators)
d_lengths = map(length, denominators)

print n_lengths
print d_lengths

print len([n for n, d in zip(n_lengths, d_lengths) if n > d])
