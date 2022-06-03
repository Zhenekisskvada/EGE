def F(n):
    print(n)
    if n >= 3:
        F(n-1)
        F(n-2)
        F(n-2)
print(F(4))