__author__ = 'stefan'

def silnia(n):
    if n==1:
        return 1
    else:
        return n*silnia(n-1)

print silnia(40)/(silnia(20)*silnia(20))


