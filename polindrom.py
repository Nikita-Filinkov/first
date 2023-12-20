x = int(input("Введите число: "))
f = int(x)
c = []
b = []
while x != 0:
    a = x % 10
    x = x // 10
    c.append(a)
    b.insert(0, a)
if c == b:
    print(f"Число {f} палиндром")
else:
    print(f"Число {f} не палиндром")
