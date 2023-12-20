questions = {
    "Транспорт": {
        "100": {"question": "plane", "answer": "самолёт", "asked": False},
        "200": {"question": "train", "answer": "поезд", "asked": False},
        "300": {"question": "bike", "answer": "велосипед", "asked": False}
    },
    "Животные": {
        "100": {"question": "cat", "answer": "кошка", "asked": False},
        "200": {"question": "bird", "answer": "птица", "asked": False},
        "300": {"question": "marten", "answer": "куница", "asked": False},
    },
    "Еда": {
        "100": {"question": "fried eggs", "answer": "яичница", "asked": False},
        "200": {"question": "roast", "answer": "жаркое", "asked": False},
        "300": {"question": "grilled meat", "answer": "жаренное мясо", "asked": False},
    },
}
points = 0
i = 0
answers = []


def show_field():
    for q in questions:
        print(f"\n{q}".ljust(len(max(questions)) + 1), end=" ")
        for key in questions[q]:
            if not questions[q][key]["asked"]:
                print(key, end=" ")
            else:
                print("   ", end=" ")


def check(i):
    for q in questions:
        for d in questions[q]:
            i += 1
    c = i
    return c


def parse_input(input_words):
    a = input_words.split(" ")
    # first_word = a[0]
    # second_word = a[1]
    return a


def show_question(a):
    if a[0] not in questions:
        return print("Такого вопроса нет попробуйте еще раз")
    for key, item in questions[a[0]].items():
        if key == a[1]:
            return print("Слово " + item["question"] + " в переводе означает")
    return print("Такого вопроса нет попробуйте еще раз")


def change_dict(a):
    questions[a[0]][a[1]]["asked"] = True
    return questions


def check_points(answer, points):
    if answer == questions[parse_input(input_words)[0]][parse_input(input_words)[1]]["answer"]:
        points += int(parse_input(input_words)[1])
    else:
        points -= int(parse_input(input_words)[1])
    return points


def check_answer(answer, a, points):
    if questions[a[0]][a[1]]["answer"] == answer:
        return print(f"Верно + {int(a[1])}, ваш счёт = {check_points(answer, points)}")
    return print(
        f"Неверно - {int(a[1])}, на самом деле {questions[a[0]][a[1]]['answer']}, ваш счёт = {check_points(answer, points)}")

# def show_stats(answer):
#     answers = []
#     if answer != questions[parse_input(input_words)[0]][parse_input(input_words)[1]]['answer']:
#         answers = answers.append(False)
#     else:
#         answers = answers.append(True)
#     return answers


for s in range(check(i)):
    while True:
        show_field()
        input_words = input("\n").title()
        if parse_input(input_words)[0] not in questions:
            print("Такого вопроса нет попробуйте еще раз")
            continue
        elif parse_input(input_words)[1] not in questions[parse_input(input_words)[0]]:
            print("Такого вопроса нет попробуйте еще раз")
            continue
        elif questions[parse_input(input_words)[0]][parse_input(input_words)[1]]["asked"]:
            print("Уже было =)\nВыбри что-то другое")
            continue
        else:
            break
        # parse_input(input_words)
    show_question(parse_input(input_words))
    answer = input("Введите слово: ")
    check_answer(answer, parse_input(input_words), points)
    points = check_points(answer, points)
    change_dict(parse_input(input_words))
    if answer != questions[parse_input(input_words)[0]][parse_input(input_words)[1]]['answer']:
        answers.append("1")
    else:
        answers.append("2")
print("У нас закончились вопросы!\n")
print(f"Ваш счёт: {points}\nВерных ответов: {answers.count('1')}\nНе верных ответов: {answers.count('2')}")
