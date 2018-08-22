__author__ = 'stefan'
def sumOfFactors(n):
    if n==0:
        return 0
    output = list(set(reduce(list.__add__,
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    output.remove(n)
    return sum(output)

sums=[]
for i in range(10000):
    print i
    sums.append(sumOfFactors(i))
total=0
for i in range(10000):
    print i
    for j in range(i+1, 10000):
        if sums[i]==j and sums[j]==i:
            total+=i+j
print total