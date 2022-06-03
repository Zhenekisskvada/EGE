def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return f(n-1)*3 - f(n-2)*2
print(f(7))