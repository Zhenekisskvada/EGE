print('x y z w f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = int(((w<=(not x))==(z<=y)) and (y or w))
                print(x,y,z,w,f)