import random

sentences = ["cat", "sky", "dark", "sun", "rock"]

morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

answers = []


def get_word():
    random.shuffle(sentences)
    random_word = sentences[0]
    return random_word


def morse_encode(word):
    for key, item in morse.items():
        if key in word:
            word = word.replace(key, item)
    return word


def print_statistics(answers):
    print(f"Всего задачек: {answers.count(True) + answers.count(False)}")
    print(f"Отвеченно верно: {answers.count(True)}")
    print(f"Отвеченно неверно: {answers.count(False)}")


print("Сегодня мы потренируемся рассшифровывать морзянку. Если захотите завершить тренеровку введите 1\nДля запуска тренеровки нажмите Enter и начнём")
input()
while True:
    word = get_word()
    # Использовать для подсказки :)
    # print(word)
    print(f"Разгадайте вот это слово: {morse_encode(word)}")
    answer = input().lower()
    if answer == word:
        answers.append(True)
        print("Правильно\n")
    elif answer == "1":
        break
    else:
        answers.append(False)
        print("Ошибка\n")


print_statistics(answers)



