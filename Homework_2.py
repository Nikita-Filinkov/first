questions = ["My name___Vova", "I___a coder", "I live___Moscow"]
answers = ["is","am","in"]
num = 0
print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать! ")
bigining_of_start = str(input())
if bigining_of_start != str("ready"):
    print("Кажется, вы не хотите играть. Очень жаль")
else:
    question_index = range(len(questions))
    for question in question_index:
        print(questions[question])
        answer_1 = str(input())
        if answer_1 == answers[question]:
            print("Ответ верный!")
            num+=1
        else:
            print(f"Неправильно. Правильный ответ: {answers[question]}")
print(f"Вот и все! Вы ответели на {num} вопросов из {len(questions)}, верно это {(num*100)/3} процентов.")






