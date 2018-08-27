nominator = 1
denominator = 1
for i in range(12, 100):
    if i % 10 == 0 or i % 11 == 0: continue
    for j in range(i, 100):
        if j % 10 == 0 or j%11 == 0 or i == j: continue
        if str(i)[0] in str(j) and \
                (float(str(i)[1]) / int(str(j).replace(str(i)[0], ''))) == float(i) / j:
            nominator *= i
            denominator *= j
            print i, j
        elif str(i)[1] in str(j) and \
                (float(str(i)[0]) / int(str(j).replace(str(i)[1], ''))) == float(i) / j:
            nominator *= i
            denominator *= j
            print i, j
        else:
            continue

print float(nominator)/denominator
