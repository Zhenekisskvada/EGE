for x in range(1,1000):
    y = (343**5) + (7**3) - 1 - x
    k = 0
    z = y
    s = ''
    while y>0:
        s = str(y%7) + s
        y = y//7
    if s.count('6') == 12:
        print(x)
        break
        
