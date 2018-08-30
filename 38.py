def is_pndigital(n):
    return len(str(n)) == 9 and not '123456789'.strip(str(n))

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
maximum = 0
index = 0
for i in range(1, 10000):
    n = 0
    output = ''
    while len(output) < 9:
        output += str(i*nums[n])
        n += 1
        print output
    if is_pndigital(output):
        if int(output) > maximum:
            maximum = int(output)
            index = i
print maximum, index
