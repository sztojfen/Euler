def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

limit = 1000000
is_prime = [False] * limit
for i in primes_sieve(limit):
    is_prime[i] = True

print is_prime

a_max = b_max = 0
maximum = 0

for a in range(-1000, 1000):
    for b in range(2, 1000):
        n = 0
        while is_prime[n ** 2 + a * n + b]:
            print n ** 2 + a * n + b
            n += 1
        if n-1 > maximum:
            maximum = n
            a_max = a
            b_max = b

print a_max, b_max, maximum, a_max*b_max