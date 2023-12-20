swers = ["is", "am", "in"]
num = 0
points = 3
tries = 3
num_question = 0
print("Привет, го сыграем в английский! Наберите go, если готовы")
start_word = input()
if start_word != str("go"):
    print("Значит ты выбрал смерть")
else:
    questions_index = range(len(questions))
    for question in questions_index:
        print(questions[question])
        num_question += 1
        answer_1 = input()
        for i in range(3, 0, -1):
            if answer_1 != answers[question]:
                points -= 1
                if num_question == 1:
                    points_1f = int(i-1)
                    points_1r = 0
                elif num_question == 2:
                    points_2f = int(i-1)
                    points_2r = 0
                elif num_question == 3:
                    points_3f = int(i-1)
                    points_3r = 0
                if i-1 == 0:
                    points_1f = 0
                    points_2f = 0
                    points_3f = 0
                    print(f"Увы, но нет. Верный ответ: {answers[question]}")
                    break
                print(f"Неправильно: осталось попыток {i - 1}, попробуйте ещё раз")
                answer_1 = input()
                points -= 1
            elif answer_1 == answers[question]:
                print("Отлично ты справился и ответил верно!")
                num += 1
                if num_question == 1:
                    points_1r = int(i)
                    points_1f = 0
                elif num_question == 2:
                    points_2r = int(i)
                    points_2f = 0
                elif num_question == 3:
                    points_3r = int(i)
                    points_3f = 0
                break
if num != 0:
    all_points = points_1r + points_2r + points_3r + points_1f + points_2f + points_3f
    print(f"Поздравляю ты ответил на {num} вопросов из {len(questions)}, вы набрали {all_points} баллов")
else:
    print("Теперь мы знаем что ты даун :)")