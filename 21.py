def f(k1,k2,n):
    #победа Петя 3 ходом
    if k1+k2>=107 and (n == 2 or n == 4):
        return 1
    #иначе Петя не выигрывает
    elif k1+k2>=107 or n>=4:
        return 0
    #Делаем ход
    n += 1
    #проверяем чей ход
    #Если ход Пети, то любая ветка приводит к победе
    if n%2==0:
        return f(k1+1,k2,n) or f(k1,k2+1,n) or f(k1*2,k2,n) or f(k1,k2*2,n)
    else:
        return f(k1+1,k2,n) and f(k1,k2+1,n) and f(k1*2,k2,n) and f(k1,k2*2,n)
for s in range(1,93+1):
    if f(13,s,0):
        print(s)
