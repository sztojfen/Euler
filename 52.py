import time

start = time.time()

def have_the_same_digits(num1, num2, num3, num4, num5, num6):
    return not (not (set(str(num1)) == set(str(num2)) == set(str(num3)) \
                     == set(str(num4)) == set(str(num5)) == set(str(num6))) \
                or not (len(str(num1)) == len(str(num2)) == len(str(num3)) == \
                    len(str(num4)) == len(str(num5)) == len(str(num6))))

found = False
n = 1
while not found:
    if str(n)[0] != "1":
        n += 1
        continue
    if have_the_same_digits(n, 2*n, 3*n, 4*n, 5*n, 6*n):
        found = True
    n += 1

print time.time() - start
