k = 0
for A in range(0,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if (((x<6)<=(x*x<A)) and ((y*y<=A)<=(y<=6))) ==0:
                f = 0
        if f ==0:
            break
    if f:
        k += 1
print(k)

