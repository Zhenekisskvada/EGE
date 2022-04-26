print('x y z f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = int(x==y or (y or z)<=x)
            if f==0:
                print(x,y,z,f)

