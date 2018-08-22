__author__ = 'stefan'
max=0
for i in range(1000000)[1:]:
    n=i
    steps=0
    while n != 1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        steps+=1
    if steps>max:
        print i
        print steps
        max=steps
print max

