for A in range(0,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if ((x*5 + y*3 != 60) or ((A>x) and (A>y)))==0:
                f=0
        if f == 0:
            break
    if f:
        print(A)
        break


