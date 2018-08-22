a = 1001
x = y = (a-1)/2
number = 1
table = [[0 for m in xrange(a)] for n in xrange(a)]
table[y][x] = number

for r in xrange(3, a+1, 2):
    x += 1
    number += 1
    table[y][x] = number
    for i in xrange(r-2):
        y += 1
        number += 1
        table[y][x] = number
    for i in xrange(r-1):
        x -= 1
        number += 1
        table[y][x] = number
    for i in xrange(r-1):
        y -= 1
        number += 1
        table[y][x] = number
    for i in xrange(r-1):
        x += 1
        number += 1
        table[y][x] = number

sum = 0
for i in xrange((len(table)-1)/2):
        sum += table[i][i]
        sum += table[len(table)-i-1][i]
        sum += table[i][len(table)-i-1]
        sum += table[len(table)-i-1][len(table)-i-1]
sum += 1

print sum



