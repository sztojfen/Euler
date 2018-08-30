from primes import primes_sieve_gen

limit = 10000000
primes = [x for x in primes_sieve_gen(limit)]

def is_pandigital(n, l):
    return len(str(n)) == l and not '1234567890'[:l].strip(str(n))

maximum = 0
for prime in primes:
    print prime
    if is_pandigital(prime, len(str(prime))):
       if prime > maximum:
           maximum = prime

print maximum