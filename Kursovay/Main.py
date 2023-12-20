from Kursovay.utils import create_examples_class
from Player import Player


def main():
    exampl = create_examples_class()
    print("Давай начнём игру!")
    user_name = input("Введите ваше имя: ")
    player1 = Player(user_name)
    print(f"Привет {player1.name}")
    print(f"Составте {exampl.count_subwords()} слов из слова {exampl.word}\nСлова не должны быть короче {exampl.min_len_subwords()} ")
    print("Чтобы закончить игру введите: стоп\nПоехали ваше первое слово?")
    while exampl.count_subwords() != player1.count_user_answer():
        user_answer = input("Поле ответа:")
        player1.user_answer = user_answer
        if player1.user_answer == "стоп" or player1.user_answer == "stop":
            break
        if len(player1.user_answer) < exampl.min_len_subwords():
            print("Слишком короткое слово")
            continue
        if not exampl.is_correct(player1.user_answer):
            print("Неверно")
            continue
        if player1.exame_return_answer():
            print("Это слово уже было использовано")
            continue
        print(player1.add_user_answer())
        print("Хороший ответ")
    print(f"Игра окончена вы угадали {player1.count_user_answer()} из {exampl.count_subwords()}")


main()
