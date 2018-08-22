def proper_divisors(n):
    return [x for x in range(1, n/2 + 1) if n % x == 0]

def abundands(n):
    return [x for x in range(12, n+1) if sum(proper_divisors(x)) > x]

if __name__ == '__main__':
    total = 0
    list_abunds = set(abundands(28123))
    dict_abunds = {x:x for x in list_abunds}

    for i in range(1, 28123):
        flag = True
        for k in list_abunds:
            if k < i:
                if (i-k) in dict_abunds:
                    flag = False
                    break;
            else:
                break
        if flag: total += i

    print total
