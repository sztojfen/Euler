from primes import primes_sieve, primes_sieve_gen

primes = [x for x in primes_sieve_gen(1000000)]
is_prime = primes_sieve(1000000)

largest = 0
length_of_largest = 0
inner_loop_len = len(primes)

for i in xrange(len(primes)):
    for j in xrange(i+length_of_largest, inner_loop_len): #dont check shorter, than we already know is a probable solution
        ans = sum(primes[i:j])
        if ans < 1000000:
            if is_prime[ans]:
                length_of_largest = j - i
                largest = ans
        else:
            inner_loop_len = j + 1 #starting with bigger i will make the number of primes that add to number bigger than 1000000 j+1
            break

print largest, length_of_largest

