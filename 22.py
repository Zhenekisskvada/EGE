for i in range(1, 10000):
  x = i
  m = 0
  s = 0
  while x > 0:
    d = x % 8
    s += d
    if d > m:
      m = d
    x = x // 8
  #print(m, s)
  if m == 5 and s == 12:
    print(i)
    break
