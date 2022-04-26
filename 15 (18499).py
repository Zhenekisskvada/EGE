for a in range(0,500):
    f = 1
    for m in range(0,500):
        for n in range(0,500):
            if ((m*2 + n*3 > 40) or ((m<a) and (n<=a))) ==0:
                f = 0
        if f == 0:
            break
    if f:
        print(a)
        break