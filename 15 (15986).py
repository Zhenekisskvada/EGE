for a in range(0,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if ((y+x*2!=48) or (a<x) or (x<y)) == 0:
                f = 0
        if f !=1:
            break
    if f:
        print(a)
