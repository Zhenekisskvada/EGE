k = 0
def f(n):
    if n>0:
        g(n-1)
def g(n):
    global k
    k+=1
    if n>1:
        f(n-2)
f(11)
print(k)