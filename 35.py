from primes import primes_sieve, primes_sieve_gen

limit = 1000000
prime_list = []
is_prime = primes_sieve(limit)
for i in primes_sieve_gen(limit):
    prime_list.append(i)

def rotate(n, l):
    return n[l:] + n[:l]

def get_rotations(n):
    for r in range(len(n)):
        yield rotate(n, r)

numbers = ['2', '4', '5', '6', '8']
result = set()
for i in prime_list:
    if any(l in numbers for l in str(i)) and i != 2 and i != 5:
        continue
    if all([is_prime[int(x)] for x in list(map(''.join, get_rotations(str(i))))]):
        for a in list(map(''.join, get_rotations(str(i)))):
            result.add(int(a))

print result, len(result)




