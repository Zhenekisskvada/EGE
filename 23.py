m = [0] * 16
m[2] = 1
for i in range(3, 11):
    m[i] += m[i - 1]
    m[i] += m[i - 2]
    if i % 3 == 0:
        m[i] += m[i // 3]
# print(m)
for i in range(11, 16):
    if i != 14:
        m[i] += m[i - 1]
        if i - 2 >= 10:
            m[i] += m[i - 2]
        if i % 3 == 0 and i // 3 >= 10:
            m[i] += m[i // 3]
print(m)
