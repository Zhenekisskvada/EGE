def f(k1, n):
    if k1 >= 76 and (n == 2 or n == 4):
        return 1
    elif k1 >= 76 or n >= 4:
        return 0
    n += 1
    if n % 2 == 0:
        return f(k1 + 1, n) or f(k1 + 2, n) or f(k1 * 3, n)
    else:
        return f(k1+1, n) and f(k1+2, n) and f(k1*3, n)
for s in range(1,75+1):
    if f(s, 0):
        print(s)
        break
