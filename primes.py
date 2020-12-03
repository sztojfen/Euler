def primes_sieve_gen(limit):
    '''Returns a generator of prime numbers'''
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False


def primes_sieve(limit):
    '''Retuns table of True/False, index is the number verified'''
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
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

if __name__ == "__main__":
    primes = primes_sieve_gen(10)
    print {i for i in primes}

    print primes_sieve(10)
