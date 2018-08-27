def is_ok(n):
    return len(str(n)) == 9 and not "123456789".strip(str(n))

result = set()
for i in range(2, 99):
    k = 1234 if i < 10 else 123
    for j in range(k, 10000/i):
        if is_ok(str(i)+str(j)+str(i*j)):
            result.add(i*j)

print sum(result)
