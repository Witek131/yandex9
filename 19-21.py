def f(n, p):
    if p % 2 != 0 and n>=105:
        return 1
    if n >= 97 and n < 105:
        return p % 2 == 0
    if p == 0 or n > 105:
        return 0
    h = [f(n + 3, p - 1), f(n + 5, p - 1), f(n * 3, p - 1)]
    return any(h) if p % 2 != 0 else all(h)


print([i for i in range(1, 96) if f(i, 2) and not f(i,1)])
print([i for i in range(1, 96) if f(i, 3) and not f(i, 1)])
print([i for i in range(1, 96) if f(i, 4) and  not f(i, 2)])
