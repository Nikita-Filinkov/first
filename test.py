a = [
        "пони", "тон", "ион", "опт", "пот", "тип", "пион", "понт"
    ]
b = []
while True:
    answer = input("Введите слолово: ")
    if answer == "стоп":
        break
    if answer in b:
        print("такое слово уже было использовано")
    if answer in a:
        b.append(answer)
        print("Слово есть в списке")
    else:
        print("слова нет в списке")
