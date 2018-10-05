from primes import primes_sieve, primes_sieve_gen

limit = 1000000
primes = [x for x in primes_sieve_gen(10000)]
is_prime = primes_sieve(1000000)
squares = [i*i for i in range(1, 100)]

first = [i for i in range(2, limit) if not i % 2 == 0 and not is_prime[i]]
second = [False] * limit
for i in first:
    second[i] = True

for i in primes:
    for j in squares:
        second[i+2*j] = False

print second.index(True)