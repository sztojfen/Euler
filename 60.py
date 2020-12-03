# BRUTE FORCE WITH SOME OPTIMIZATION (51 seconds on MacBook Air 2018)

from primes import primes_sieve, primes_sieve_gen, is_prime
import itertools
import time


class Euler60(object):
    def __init__(self):
        self.limit = 10000
        self.primes_table = [x for x in primes_sieve_gen(self.limit)]
        self.result = 5 * self.limit
        self.pairs = {}
        self.primes = []

    def generate_matching_primes(self, prime):
        """ Returns table of primes greater than argument that concatenated
        with argument (no matter the order) also give prime"""
        pairs = [x for x in self.primes_table if
                 x > prime and
                 is_prime(int(str(prime) + str(x))) and
                 is_prime(int(str(x) + str(prime)))]
        return pairs

    def e60(self):
        start = time.time()
        for (ai, a) in enumerate(self.primes_table):
            if 5*a > self.result: break
            if not self.pairs.get(str(a)):
                self.pairs[str(a)] = self.generate_matching_primes(a)

            for (bi, b) in enumerate(itertools.islice(self.primes_table, ai+1, len(self.primes_table))):
                if a + 4*b > self.result: break
                if b not in self.pairs[str(a)]: continue
                if not self.pairs.get(str(b)):
                    self.pairs[str(b)] = self.generate_matching_primes(b)

                for (ci, c) in enumerate(itertools.islice(self.primes_table, ai+bi+2, len(self.primes_table))):
                    if a + b + 3*c > self.result: break
                    if c not in self.pairs[str(a)] or c not in self.pairs[str(b)]: continue
                    if not self.pairs.get(str(c)):
                        self.pairs[str(c)] = self.generate_matching_primes(c)

                    for (di, d) in enumerate(itertools.islice(self.primes_table, ai+bi+ci+3, len(self.primes_table))):
                        if a + b + c + 2*d > self.result: break
                        if d not in self.pairs[str(a)] or d not in self.pairs[str(b)] or d not in self.pairs[str(c)]:
                            continue
                        if not self.pairs.get(str(d)):
                            self.pairs[str(d)] = self.generate_matching_primes(d)

                        for (ei, e) in enumerate(
                                itertools.islice(self.primes_table, ai+bi+ci+di+4, len(self.primes_table))):
                            if a + b + c + d + e > self.result: break
                            if e not in self.pairs[str(a)] or e not in self.pairs[str(b)] or \
                                            e not in self.pairs[str(c)] or e not in self.pairs[str(d)]:
                                continue

                            if self.result > a + b + c + d + e:
                                self.result = a + b + c + d + e
                                self.primes = [a, b, c, d, e]

        print self.result
        print self.primes
        end = time.time()
        print end-start

e60 = Euler60()
e60.e60()

# ProjectEuler FORUM SOLUTION:

# from copy import copy
# from math import sqrt
#
# primes = [2,3,5,7,11,13]
# def nextprime():
#     next_num = primes[-1] + 2
#     nnsqrt = int(sqrt(next_num))
#     isprime = False
#     while not isprime:
#         isprime = True
#         for prime in primes:
#             if prime > nnsqrt: break
#             if next_num % prime == 0:
#                 next_num += 2
#                 isprime = False
#                 break
#     primes.append(next_num)
#     return next_num
#
# def is_prime(num):
#     # Uncommenting the following line approximately doubles
#     # the time taken for this program!
#     #if num in primes: return True
#     nsqrt = int(sqrt(num))
#     if num == nsqrt * nsqrt: return False
#     last_prime = primes[-1]
#     # Make sure we have enough prime numbers to test this.
#     while last_prime < nsqrt:
#         last_prime = nextprime()
#     for prime in primes:
#         if prime > nsqrt: break
#         if num % prime == 0: return False
#     return True
#
# concatmem = {}
# def concat2(a, b):
#     # NB: Always called with a > b.
#     key_pair = (a, b)
#     if key_pair in concatmem: return concatmem[key_pair]
#     stra = str(a)
#     strb = str(b)
#     result = is_prime(int(stra + strb)) \
#          and is_prime(int(strb + stra))
#     concatmem[key_pair] = result
#     return result
#
# def concat(set, lvl):
#     # 'set' is a five-element list, but we only want to
#     # compare elements set[0]..set[lvl-1] with set[lvl]
#     for i in xrange(lvl):
#         if not concat2(set[i], set[lvl]): return False
#     return True
#
# def find_set():
#     min_sum_start = 999999999999 # Large enough?
#     min_sum = min_sum_start
#     i = 4
#     set = [0, 0, 0, 0, 0]
#     while True:
#         i += 1
#         # primes should get bigger faster than I need it.
#         set[0] = primes[i]
#         for j in xrange(i - 1, 3, -1):
#             set[1] = primes[j]
#             if not concat(set, 1): continue
#             for k in xrange(j - 1, 2, -1):
#                 set[2] = primes[k]
#                 if not concat(set, 2): continue
#                 for l in xrange(k - 1, 1, -1):
#                     set[3] = primes[l]
#                     if not concat(set, 3): continue
#                     for m in xrange(l - 1, 0, -1):
#                         set[4] = primes[m]
#                         if not concat(set, 4): continue
#                         sum_set = sum(set)
#                         if min_sum > sum_set:
#                             min_sum = sum_set
#                             min_set = copy(set)
#         if min_sum < min_sum_start: return min_sum, min_set
#
# sum_of_set, set = find_set()
# print 'Sum of prime set:', sum_of_set, ' Prime set:', set