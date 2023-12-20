x = [9]
y = []
z = []
b = []
v = []
for i in x:
    y.append(f"{i}")
f_1 = ''.join(y)
f_2 = int(f_1)
while f_2 != 0:
    a = f_2 % 10
    f_2 = f_2 // 10
    b.insert(0, a)
for o in b:
    z.append(f"{o}")
d_1 = ''.join(z)
d_2 = int(d_1) + 1
while d_2 != 0:
    c = d_2 % 10
    d_2 = d_2 // 10
    v.insert(0, c)
print(v)
