print('x y z w f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = int(((x and w) or (w and z))==((z<=y) and (y<=x)))
                if f==1:
                    print(x,y,z,w,f)