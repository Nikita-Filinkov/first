print("Привет! Предлагаю проверить свои знания анлийского!")
name = input("Расскажи, как тебя зовут? ")
print(f"Привет,{name}, начинаем тренеровку! ")
print("My name___Vova ")
answer_1 = input("Введите ответ: ")
if answer_1 == str("is"):
    question_1 = 10
    right_answer_1 = 1
    print('''Ваш ответ верный!
Вы получаете 10 баллов!''')
else:
    question_1 = 0
    right_answer_1 = 0
    print('''Неправильно.
Правильный ответ: is''')
print("I ____ a coder ")
answer_2 = input("Введите ответ: ")
if answer_2 == str("am"):
    question_2 = 10
    right_answer_2 = 1
    print('''Ваш ответ верный!
Вы получаете 10 баллов!''')
else:
    question_2 = 0
    right_answer_2 = 0
    print('''Неправильно.
Правильный ответ: am''')
print("I ____ a coder ")
answer_3 = input("Введите ответ: ")
if answer_3 == str("in"):
    question_3 = 10
    right_answer_3 = 1
    print('''Ваш ответ верный!
Вы получаете 10 баллов!''')
else:
    question_3 = 0
    right_answer_3 = 0
    print('''Неправильно.
Правильный ответ: in''')
all_right_answer = right_answer_1 + right_answer_2 + right_answer_3
sum_questions = question_1 + question_2 + question_3
persent_right_question = (sum_questions * 100) / 30
if sum_questions == 30:
    print(f"Вы ответили верно на {all_right_answer} вопроса из 3 верно")
    print(f"Вы заработали {sum_questions} баллов")
    print(f"Это {persent_right_question} процентов")
elif sum_questions == 20:
    print(f"Вы ответили верно на {all_right_answer} вопроса из 3 верно")
    print(f"Вы заработали {sum_questions} баллов")
    print(f"Это {persent_right_question} процентов")
elif sum_questions == 10:
    print(f"Вы ответили верно на {all_right_answer} вопроса из 3 верно")
    print(f"Вы заработали {sum_questions} баллов")
    print(f"Это {persent_right_question} процентов")
elif sum_questions == 0:
    print(f"Вы ответили верно на {all_right_answer} вопроса из 3 верно")
    print(f"Вы заработали {sum_questions} баллов")
    print(f"Это {persent_right_question} процентов")