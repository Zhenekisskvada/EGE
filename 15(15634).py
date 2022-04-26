for A in range(0,500):
    f = 1
    for x in range(0,500):
        for y in range(0,500):
            if (((y + 2*x)<A) or (x>30) or (y>20)) ==0:
                f = 0
                break
    if f:
        print(A)
        break
