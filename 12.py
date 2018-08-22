__author__ = 'stefan'

def numberOfFactors(n):
    if n==0:
        return 0
    return len(set(reduce(list.__add__,
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def triangleNumber(n):
    result=0
    while n>=1:
        result+=n
        n-=1
    return result

for i in range(100000):
    if numberOfFactors(triangleNumber(i))>500:
        print triangleNumber(i)


