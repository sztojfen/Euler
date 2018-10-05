from primes import primes_sieve
import itertools

is_prime = primes_sieve(9999)


def check_sequence(a):
    prime_set = [int("".join(x)) for x in itertools.permutations(str(a)) if is_prime[int("".join(x))]]

    l = len(prime_set)
    if l >= 3:
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    a = prime_set[k] - prime_set[j]
                    if a == prime_set[j] - prime_set[i] and a > 0:
                        print prime_set[i], prime_set[j], prime_set[k]
                        return True
    return False

for i in range(1488, 9999):
    check_sequence(i)

