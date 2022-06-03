k = 0
for A in range(-500,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if (((x<A)<=(x**2<81) and ((y**2<=36)<=(y<=A)))) ==0:
                f = 0
        if f==0:
            break
    if f:
        k+=1
print(k)
