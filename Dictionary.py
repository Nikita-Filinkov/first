easy = {"cat": "кошка", "sky": "небо", "dark": "тьма", "sun": "солнце", "rock": "камень"}
mediume = {"wight": "вес", "weak": "слабый", "pool": "бассейн", "arm": "рука", "smile": "улыбка"}
hard = {"quality": "качество", "pressure": "давление", "apologize": "извиняться", "death": "смерть", "supernatural": "сверхъестественное"}
levels = {0: "Нулевой уровень",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}
answers = {}
key_levels = 0
print("Выберните уровень сложности\nДоступны следущие уровни:\neasy\nmediume\nhard ")
a = input().lower()
if a == "easy":
    words = easy
elif a == "mediume":
    words = mediume
elif a == "hard":
    words = hard
else:
    print("Такого уровня не предусмотрено")
print(f"Выбран уровень сложности, мы предложим {len(words)} слов, подберите перевод")
for word in words:
    input("Нажмите Enter: ")
    print(f"{word}, {len(words[word])} букв, начинается с {words[word][0]}...")
    b = input().lower()
    if b == words[word]:
        print(f"Верно, {word} это {words[word]} ")
        answers[word] = True
        key_levels += 1
    else:
        print(f"Неверно, {word} это {words[word]}")
        answers[word] = False
if key_levels > 0:
    print(f"Правильно отвечены слова: ")
    for answer in answers:
        if answers[answer] == True:
            print(f"{answer}")
elif key_levels == 0:
    print(f"Правильно отвеченных слов нет ")
if key_levels < 5:
    print(f"Неправильно отвечены слова: ")
    for answer in answers:
        if answers[answer] == False:
            print(f"{answer}")
elif key_levels == 5:
    print("Непраильно отвеченных слов нет")
print(f"Ваш ранг: {levels[key_levels ]}")