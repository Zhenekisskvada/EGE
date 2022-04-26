def f(n):
    if n<=2:
        return n+1
    if n>2:
        return f(n-1)+2*f(n-2)
n = int(input())
print(f(n))