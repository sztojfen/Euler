def _25():
    fib = [1, 1]
    elem = 0
    i = 2
    while len(str(elem)) < 1000:
        elem = fib[i-1] + fib[i-2]
        fib.append(elem)
        i += 1
    return i

print _25()
