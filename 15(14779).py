k = 0
for A in range(-500,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if (((x<5)<=(x**2<A)) and ((y**2<=A)<=(y<=5)))==0:
                f = 0
        if f ==0:
            break
    if f:
        k +=1
print(k)