s = 0
def F(n):
    if n > 0:
        global s
        F(n - 4)
        s = s+n
        F(n // 3)
F(9)
print (s)

