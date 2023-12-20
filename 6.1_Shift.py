alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift_encode(word, step):
    word_encode = ""
    for letter in word:
        place = alphabet.find(letter)
        next_letter = (place + step) % len(alphabet)
        word_encode += alphabet[next_letter]

    return word_encode


def shift_decode(word, step):
    word_decode = ""
    for letter in word:
        place = alphabet.find(letter)
        word_decode += alphabet[place - step]
    return word_decode


word = input("Введите слово для шифорования: ")
step = int(input("Введите шаг шифрования: "))

print(f"Зашифрованное слово: {shift_encode(word, step)}")
print(f"Дешифрованное слово: {shift_decode(shift_encode(word, step), step)}")


def check_mail(word, simbols):
    i = -1
    for c in simbols:
        i = word.find(c, i + 1)
        if i == -1:
            print(f"В почте не хватает обязательных символов из списка: {simbols}")
            break
    return print("Хорошая почта!")

