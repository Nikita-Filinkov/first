a = ["dear", "down", "sands","deger", "rtder" "south"]
b = input("введите букву ")
for i in range(len(a)):
    if b in a[i][:len(b)]:
        print(a[i])
