print ('x y z f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = int((x==z) or (x<=(y and z)))
            if f==0:
                print (x,y,z,f)