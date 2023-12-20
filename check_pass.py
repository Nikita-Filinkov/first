alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
numbers = "0123456789"
a = input("Введите пароль:")


def check_pass(x):
    input_word = x
    if len(x) < 8:
        print("Пин меньше 8 символов")
    else:
        input_word_a = ""
        input_word_n = ""
        for i in x:
            if i in alphabet:
                input_word_a += i
            elif i in numbers:
                input_word_n += i
            else:
                return print("Не допустимые символы")
        if input_word == input_word_a:
            print("Пароль не должен содержать одинаковые типы символов")
        elif input_word == input_word_n:
            print("Пароль не должен содержать одинаковые типы символов")
        elif input_word != input_word_a and input_word_n:
            print("Допустимый пароль")


check_pass(a)
