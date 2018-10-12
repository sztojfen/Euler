from primes import primes_sieve, primes_sieve_gen
import itertools

def has_at_least_3_same_digits(number):
    d = {}
    for letter in str(number):
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] += 1
    return max(d.itervalues()) >= 3


limit = 1000000

primes = [x for x in primes_sieve_gen(limit)]
primes = primes[primes.index(56003) - 1:]
is_prime = primes_sieve(limit)

replacement_digits = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

def calculate():
    found = False
    already_checked = []
    counter = 10
    while not found:
        prime = primes.pop(0)
        if not has_at_least_3_same_digits(prime):
            continue
        print prime
        for n_of_digits in xrange(3, len(str(prime)), 3):
            for sequence in set(["".join(c) for c in
                                 itertools.combinations('0123456789'[:len(str(prime))-1], n_of_digits)]):
                temp = list(str(prime))
                if counter < 8:
                    for elem in already_checked:
                        if elem in primes:
                            primes.remove(elem)
                    already_checked = []
                counter = 0
                for x in replacement_digits:
                    if sequence:
                        for i in sequence:
                            temp[int(i)] = str(x)

                        if is_prime[int("".join(temp))]:
                            counter += 1
                            already_checked.append(int("".join(temp)))
                        if counter == 8 and all([len(str(q)) >= 6 for q in already_checked]):
                            if prime not in already_checked:
                                counter = 0
                                continue
                            print prime, sequence, already_checked
                            found = True
                            return

calculate()