def f(n):
    kd = 2
    d = 2
    while d * d < n:
        if n % d == 0:
            kd += 2
            if kd > 17:
                return 1
        d += 1
    if d * d == n:
        kd += 1
    if kd > 17:
        return 1
    else:
        return 0
k = 0
mi = 50003
for i in range(10001, 50001):
    if f(i):
        k += 1
        if i < mi:
            mi = i
print(k, mi)
            
