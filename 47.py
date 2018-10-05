Limit = 1000000
factors = [0] * Limit
count = 0
for i in xrange(2, Limit):
    if factors[i] == 0:  # dynamic factors calculation
        count = 0
        val = i
        while val < Limit:
            factors[val] += 1  # add 1 to all prime multipliers
            val += i
    elif factors[i] == 4:  # if a number has 4 factors...
        count += 1
        if count == 4:  # and 3 following numbers have 4 factors too
            print i - 3  # get first of 4 numbers
            print factors[i-3]
            break
    else:
        count = 0
