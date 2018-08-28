def is_palindrome(n):
    n = str(n)
    if len(n) % 2 == 0:
        return all(n[i] == n[-i-1] for i in xrange(len(n)/2))
    else:
        return all(n[i] == n[-i-1] for i in xrange(len(n)/2))

ans = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome("{0:b}".format(i)):
        ans += i

print ans

