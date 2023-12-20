questions = {
    "1": {
        "100": {"question": "plane", "answer": "1", "asked": False},
        "200": {"question": "train", "answer": "1", "asked": False},
        "300": {"question": "bike", "answer": "1", "asked": False}
    },
    "2": {
        "100": {"question": "cat", "answer": "1", "asked": False},
        "200": {"question": "bird", "answer": "1", "asked": False},
        "300": {"question": "marten", "answer": "1", "asked": False},
    },
    "3": {
        "100": {"question": "fried eggs", "answer": "1", "asked": False},
        "200": {"question": "roast", "answer": "1", "asked": False},
        "300": {"question": "grilled meat", "answer": "1", "asked": False},
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
#         answers.append("1")
#     else:
#         answers.append("2")
#     return


for s in range(check(i)):
    show_field()
    input_words = input("\n")
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

# questions = {
#     "Транспорт": {
#         "100": {"question": "plane", "answer": "самолёт", "asked": False},
#         "200": {"question": "train", "answer": "поезд", "asked": False},
#         "300": {"question": "bike", "answer": "велосипед", "asked": False},
#     },
#     "Животные": {
#         "100": {"question": "cat", "answer": "кошка", "asked": False},
#         "200": {"question": "bird", "answer": "птица", "asked": False},
#         "300": {"question": "marten", "answer": "куница", "asked": False},
#     },
#     "Еда": {
#         "100": {"question": "fried eggs", "answer": "яичница", "asked": False},
#         "200": {"question": "roast", "answer": "жаркое", "asked": False},
#         "300": {"question": "grilled meat", "answer": "жаренное мясо", "asked": False},
#     },
# }
# questions_1 = {
#     "Транспорт": {
#         "100": {"question": "plane", "answer": "самолёт", "asked": False},
#         "200": {"question": "train", "answer": "поезд", "asked": False},
#         "300": {"question": "bike", "answer": "велосипед", "asked": False},
#     },
#     "Животные": {
#         "100": {"question": "cat", "answer": "кошка", "asked": False},
#         "200": {"question": "bird", "answer": "птица", "asked": False},
#         "300": {"question": "marten", "answer": "куница", "asked": False},
#     },
#     "Еда": {
#         "100": {"question": "fried eggs", "answer": "яичница", "asked": False},
#         "200": {"question": "roast", "answer": "жаркое", "asked": False},
#         "300": {"question": "grilled meat", "answer": "жаренное мясо", "asked": False},
#     },
# }
# for q in questions:
#     print(f"\n{q}".ljust(len(max(questions)) + 1), end=" ")
#     for key in questions[q]:
#         if not questions[q][key]["asked"]:
#             # print(questions[q][key]["answer"], end=" ")
#             print(key, end=" ")
#         else:
#             print("   ", end=" ")
#
# input_words = input("\n")
#
#
# def parse_input(input_words):
#     a = input_words.split(" ")
#     # first_word = a[0]
#     # second_word = a[1]
#     return a
#
#
# def show_stats(answer):
#     answers = []
#     for key, item in questions[parse_input(input_words)[0]].items():
#         if answer != item["answer"]:
#             answers.append(False)
#         else:
#             answers.append(True)
#     return print(answers)
#
#
# answer = input(" ")
# show_stats(answer)
#
# # inputs = []
# # # for key in questions[a[0]]:
# # #     if key == a[1]:
# # #         questions[a[0]]["  "] = questions[a[0]].pop(key)
# # #     if questions[a[0]][key]["answer"] == answer:
# # #         questions[a[0]][key]["asked"] = True
# # #         questions[a[0]][key] = questions[a[0]].pop(key)
# # #     else:
# # #         questions[a[0]][key] = questions[a[0]].pop(key)
# # # questions["Транспорт"]["  "] = questions["Транспорт"].pop("100")
# # # print(questions["Транспорт"])
# #     # print(questions["Транспорт"][key]["answer"])
# # # Работает, но ставит в конец, что изменяет изначальную структуру.
# # # questions["Транспорт"]["  "] = questions["Транспорт"].pop("100")
# # # А это работает как надо. Можно же всё удалять и ставить в конец, тогда изначальная структура не изменится.
# # # for key in questions["Транспорт"]:
# # #     if key == "200":
# # #         questions["Транспорт"]["  "] = questions["Транспорт"].pop("200")
# # #     else:
# # #         questions["Транспорт"][key] = questions["Транспорт"].pop(key)
# # # print(questions)
# #
# # # def show_field():
# # #     for q in questions_1:
# # #         print(f"\n{q}".ljust(len(max(questions_1)) + 1), end=" ")
# # #         for key in questions_1[q]:
# # #             print(key, end=" ")
# # #
# # #
# # # def show_question(a):
# # #     if a[0] not in questions:
# # #         return print("Такого вопроса нет попробуйте еще раз")
# # #     for key, item in questions[a[0]].items():
# # #         if key == a[1]:
# # #             return print("Слово " + item["question"] + " в переводе означает")
# # #     return print("Такого вопроса нет попробуйте еще раз")
# # #
# # #
# # def parse_input(input_words):
# #     a = input_words.split(" ")
# #     # first_word = a[0]
# #     # second_word = a[1]
# #     return a
# #
# #
# # # def change_dict(a, answer):
# # #     while True:
# # #         if questions[a[0]][a[1]]["answer"] == answer:
# # #             questions[a[0]][a[1]]["asked"] = True
# # #             questions[a[0]]["  "] = questions[a[0]].pop(a[1])
# # #         elif questions[a[0]][a[1]]["answer"] != answer:
# # #             questions[a[0]][a[1]] = questions[a[0]].pop(a[1])
# # #         else:
# # #             questions[a[0]][a[1]]["answer"] =
# # #         return questions
# #
# # #
# # # def change_dict(a, answer):
# # #     for key, item in questions[a[0]].items():
# # #         if key in inputs:
# # #             continue
# # #         if questions[a[0]][key]["answer"] == answer:
# # #             questions_1[a[0]]["  "] = questions_1[a[0]].pop(a[1])
# # #             item["asked"] = True
# # #             inputs.append(a[1])
# # #         # else:
# # #         #     questions_1[a[0]][key] = questions_1[a[0]].pop(key)
# # #     return questions_1
# # #
# # #
# # # # def check_points(a, answer, points):
# # # #     if answer == questions[a[0]][a[1]]["answer"]:
# # # #         points -= int(a[1])
# # # #         else:
# # # #         points += int(a[1])
# # # #     for key, item in questions[a[0]][a[1]].items():
# # # #         if answer != item["answer"]:
# # # #             points -= int(a[1])
# # # #         else:
# # # #             points += int(a[1])
# # # #     return points
# # #
# # # # parse_input(input_words)
# # # # print(questions[parse_input(input_words)[0]][parse_input(input_words)[1]]["answer"])
# # #
# # # # points = 0
# # # # answer = input("Введите ответ")
# # # # if answer == questions[parse_input(input_words)[0]][parse_input(input_words)[1]]["answer"]:
# # # #     points += int(parse_input(input_words)[1])
# # # #     print(f"Все отлично: {points}")
# # # #
# # # # else:
# # # #     points -= int(parse_input(input_words)[1])
# # # #     print(f'Все отлично: {points}')
# # # while True:
# # #     show_field()
# # #     input_words = input("\n")
# # #     show_question(parse_input(input_words))
# # #     answer = input("Введите ответ: ")
# # #     change_dict(parse_input(input_words), answer)
# # input_words = input("\n")
# # answer = input("Введите слово: ")
# # parse_input(input_words)
# # for key in questions[parse_input(input_words)[0]]:
# #     if questions[parse_input(input_words)[0]][key]["answer"] == answer:
# #         questions[parse_input(input_words)[0]]["  "] = questions[parse_input(input_words)[0]].pop(key)
# #         questions[parse_input(input_words)[0]][key]["asked"] = True
# #         continue
# #         questions[parse_input(input_words)[0]][key] = questions[parse_input(input_words)[0]].pop(key)
# #     else:
# #         questions[parse_input(input_words)[0]]["  "] = questions[parse_input(input_words)[0]].pop(key)
# #         continue
# #         questions[parse_input(input_words)[0]][key] = questions[parse_input(input_words)[0]].pop(key)
