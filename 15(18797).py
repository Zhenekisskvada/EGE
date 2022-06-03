for A in range(0,100):
    f = 1
    for x in range(0,100):
        for y in range(0,100):
            if ((x>A) or (y>x) or ((y*2 + x) < 110))==0:
                f = 0
        if f==0:
            break
    if f:
        print(A)