print('x y z w f')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = int((x==(w or y)) or ((w<=z) and (y<=w)))
                if f == 0:
                    print(x,y,z,w,f)
