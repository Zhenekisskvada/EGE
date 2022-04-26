print ('x y z f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = int(not(x) and y and z or not(x) and not(y) and z or not(x) and not(y) and not(z))
            if f ==1:
                print(x,y,z,f)