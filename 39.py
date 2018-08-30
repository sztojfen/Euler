def is_right(i, j, k):
    return i**2 + j**2 == k**2 or i**2 == j**2 + k**2 or i**2 + k**2 == j**2

solutions = [0] * 1000
for i in xrange(1, 1000, 2):
    print i
    for j in range(1, 1000-i):
        for k in range(1, 1000-i-j):
            if is_right(i, j, k):
                solutions[i+j+k] += 1

print solutions.index(max(solutions))
