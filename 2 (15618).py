print('x y z w f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = int((x and not y) or (y==z) or not w)
                if f==0:
                    print(x,y,z,w,f)