import itertools

def check_conditions(str):
    return int(str[1:4]) % 2 == 0 and \
                            int(str[2:5]) % 3 == 0 and \
                            int(str[3:6]) % 5 == 0 and \
                            int(str[4:7]) % 7 == 0 and \
                            int(str[5:8]) % 11 == 0 and \
                            int(str[6:9]) % 13 == 0 and \
                            int(str[7:10]) % 17 == 0

pandigitals = [str("".join(p)) for p in itertools.permutations('1234567890') if check_conditions("".join(p))]
int_pan = [int(i) for i in pandigitals]
print sum(int_pan)
