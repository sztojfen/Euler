import time
start = time.time()

sum = 0
for x in range (1,1000):
        sum = sum + (x**x)

sum = str(sum)
print sum[-10:]

print time.time() - start