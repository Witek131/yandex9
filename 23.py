def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x > y and x % 3 != 0: return f(x - 5, y) + f(x - x % 3, y)
    if x > y and x % 3 == 0: return f(x - 5, y) + f(x // 3, y)


print(f(103, 73) * f(73, 24))
