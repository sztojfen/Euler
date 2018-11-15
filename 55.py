def is_palindrome(n):
    n = str(n)
    return all(n[i] == n[-i - 1] for i in xrange(len(n) / 2))


def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r


answers = []
for i in range(1, 10000):
    print i
    found = False
    j = 0
    while not found and j < 50:
        if is_palindrome(i + reverse_number(i)):
            found = True
        j += 1
        i = i + reverse_number(i)
        if j == 50:  # Found one!
            answers.append(i)

print len(answers)
