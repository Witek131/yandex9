def f(n):
    s = 0
    while n > 0:
        if n % 25 == 0:
            s += 1
        n //= 25
    return s


a = 25 ** 340 + 25 ** 79 - 5 ** 60
k = 0
for x in range(100000000,0, -1):
    if f(a + x) == 287:
        k = x
        break
print(k)
