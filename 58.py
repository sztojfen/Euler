def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            print i
            for n in xrange(i*i, limit, i):
                a[n] = False
    return a

def is_prime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

found = False
i = 1
num = 1
total = 1
primes = 0
while not found:
    total += 4
    if is_prime(num+2*i):
        primes += 1
    if is_prime(num+4*i):
        primes += 1
    if is_prime(num+6*i):
        primes += 1
    if is_prime(num+8*i):
        primes += 1

    ratio = float(primes) / total
    print ratio
    if ratio < .1:
        print 1 + 2 * i
        found = True
        print num + 8 * i

    num = num + 8 * i
    i += 1


# def gen_table(f):
#     a = f  # len of side
#     x = y = (a - 1) / 2  # go to center of table
#     number = 1  # first number
#     print "GENERATING"
#     table = [[0 for m in xrange(a)] for n in xrange(a)]
#     print "GENERATED"
#     table[y][x] = number  # fill middle with 1
#
#     for r in xrange(3, a + 1, 2):
#         print r
#         x += 1
#         number += 1
#         table[y][x] = number
#         for i in xrange(r - 2):
#             y -= 1
#             number += 1
#             table[y][x] = number
#         for i in xrange(r - 1):
#             x -= 1
#             number += 1
#             table[y][x] = number
#         for i in xrange(r - 1):
#             y += 1
#             number += 1
#             table[y][x] = number
#         for i in xrange(r - 1):
#             x += 1
#             number += 1
#             table[y][x] = number
#     return table
#
# side = 25001
# table = gen_table(side)
# is_prime = primes_sieve(side ** 2)
# mid = (side-1)/2
# ratio = 1.0
# a = 1
# primes = 0
# total = 1  # "1" in the middle
# while ratio > .1:
#     a += 2
#     total += 4
#
#     if is_prime[table[mid - (a-1)/2][mid - (a-1)/2]]:
#         primes += 1
#     if is_prime[table[mid - (a-1)/2][mid + (a-1)/2]]:
#         primes += 1
#     if is_prime[table[mid + (a-1)/2][mid - (a-1)/2]]:
#         primes += 1
#     if is_prime[table[mid + (a-1)/2][mid + (a-1)/2]]:
#         primes += 1
#
#     ratio = float(primes) / total
#     print ratio
#     if ratio < .1:
#         print a
