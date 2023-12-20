alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
space = " "
numbers = "0123456789"
a = input()


def check_pin(x):
    if len(x) != 4:
        print("Количество символов не равно 4")
    elif x.count(x[0]) == len(x):
        print("Число не может состоять из одинаковых элементов")
    else:
        b = ""
        for number in range(1, len(x) + 1):
            b += str(number)
        if b == x:
            print("Не допускается простая последовательность")
        else:
            print("Допустимый код")


check_pin(a)


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

word = input("Введите почту:")
simbols = "@."


def check_mail(word, simbols):
    for c in simbols:
        i = word.find(c)
        if i == -1:
            return print(f"В почте не хватает обязательных символов из списка: {simbols}")
    return print("Хорошая почта!")


check_mail(word, simbols)

name = input("Введите имя:").lower()


def check_name(name):
    for i in name:
        if i not in alphabet:
            return False
        return True


print(check_name(name))
