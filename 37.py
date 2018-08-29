from primes import primes_sieve, primes_sieve_gen


def get_truncated_right(n):
    n = str(n)
    return [int(n[:i]) for i in range(1, len(n) + 1)]


def get_truncated_left(n):
    n = str(n)
    return [int(n[i:]) for i in range(0, len(n))]


is_prime = primes_sieve(1000000)
primes = [x for x in primes_sieve_gen(10000000)]

result = []
q = 4
while len(result) < 11:
    numbers = ['2', '4', '5', '6', '8', '0']
    prime = primes[q]
    if any([l in numbers for l in str(prime)]) and prime > 100:
        q += 1
        continue

    if all([is_prime[p] for p in get_truncated_right(prime)]) and \
            all([is_prime[p] for p in get_truncated_left(prime)]):
        result.append(prime)
        print result
    q += 1
    print q

print result, sum(result)
