from primes import primes_sieve, primes_sieve_gen, is_prime
from math import log10


def generate(base):
    temp = {}
    n = 1
    while True:
        if base == 3:
            num = n*(n+1)/2
        elif base == 4:
            num = n * n
        elif base == 5:
            num = n * (3 * n - 1) / 2
        elif base == 6:
            num = n * (2 * n - 1)
        elif base ==7:
            num = n * (5 * n - 3) / 2
        elif base == 8:
            num = n * (3 * n - 2)
        n += 1
        if int(log10(num))+1 < 4:
            continue
        if int(log10(num))+1 > 4:
            break
        temp[n-1] = num
    return temp


def first_two(num):
    return num // 10 ** (int(log10(num)) - 1)


def last_two(num):
    return num % 100


def next_cycle(num1, num2):
    return last_two(num1) == first_two(num2)


def get_next_set(data, used_fig, used_bas, number):
    output = {}
    for fig in data.keys():
        output[fig] = {}

    for fig in data.keys():
        if fig in used_fig:
            continue
        for bas in data[fig].keys():
            if bas in used_bas:
                continue
            if next_cycle(number, data[fig][bas]):
                output[fig][bas] = data[fig][bas]
    has_next_set = False

    for key in output:
        if len(output[key]) > 0:
            has_next_set = True
    if has_next_set:
        return output
    else:
        return False

e61 = {3: generate(3), 4: generate(4), 5: generate(5), 6: generate(6), 7: generate(7), 8: generate(8)}

used_figurates = []
used_bases = []
result = []

for figurate1 in e61.keys():
    used_figurates.append(figurate1)
    used_bases = []
    for base1 in e61[figurate1].keys():
        # print "F: " + str(figurate1) + " N: " + str(base1)
        used_bases.append(base1)
        result = [] #reset the result
        a = get_next_set(e61, used_figurates, used_bases, e61[figurate1][base1])
        e61[figurate1][base1]
        if not a:
            used_bases.pop()
            continue
        result.append(e61[figurate1][base1])

        for figurate2 in a.keys():
            used_figurates.append(figurate2)
            for base2 in a[figurate2].keys():
                used_bases.append(base2)
                b = get_next_set(e61, used_figurates, used_bases, a[figurate2][base2])
                if not b:
                    used_bases.pop()
                    continue
                result.append(a[figurate2][base2])

                for figurate3 in b.keys():
                    used_figurates.append(figurate3)
                    for base3 in b[figurate3].keys():
                        used_bases.append(base3)
                        c = get_next_set(e61, used_figurates, used_bases, b[figurate3][base3])
                        if not c:
                            used_bases.pop()
                            continue
                        result.append(b[figurate3][base3])

                        for figurate4 in c.keys():
                            used_figurates.append(figurate4)
                            for base4 in c[figurate4].keys():
                                used_bases.append(base4)
                                d = get_next_set(e61, used_figurates, used_bases, c[figurate4][base4])
                                if not d:
                                    used_bases.pop()
                                    continue
                                result.append(c[figurate4][base4])

                                for figurate5 in d.keys():
                                    used_figurates.append(figurate5)
                                    for base5 in d[figurate5].keys():
                                        used_bases.append(base5)
                                        e = get_next_set(e61, used_figurates, used_bases, d[figurate5][base5])
                                        if not e:
                                            used_bases.pop()
                                            continue
                                        result.append(d[figurate5][base5])

                                        for figurate6 in e.keys():
                                            used_figurates.append(figurate6)
                                            for base6 in e[figurate6].keys():
                                                used_bases.append(base6)
                                                result.append(e[figurate6][base6])

                                                if next_cycle(result[5], result[0]):
                                                    print result
                                                    print used_figurates
                                                    print used_bases
                                                    print sum(result)
                                                    break

                                                result.pop()
                                                used_bases.pop()
                                            used_figurates.pop()
                                        result.pop()
                                        used_bases.pop()
                                    used_figurates.pop()
                                result.pop()
                                used_bases.pop()
                            used_figurates.pop()
                        result.pop()
                        used_bases.pop()
                    used_figurates.pop()
                result.pop()
                used_bases.pop()
            used_figurates.pop()
        result.pop()
        used_bases.pop()
    used_figurates.pop()
