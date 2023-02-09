import random as rd

welcome_phrase = 'Это игра в "Угадай Число"\nВведите число больше 1 до которого мне загадать.\n'
over_number_phrase = 'Ваше число больше загаданного, попробуйте еще разок\n'
below_number_phrase = 'Ваше число меньше загаданного, попробуйте еще разок\n'
end_game_phrase = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
invalid_predict_input_phrase = 'А может быть все-таки введем целое число от 1 до {}, у вас осталось {} попыток?\n'
invalid_input_phrase = 'Нужно ввести число больше 1, у вас осталось {} попыток.\n'
win_game_phrase = 'Вы угадали с {} попытки, поздравляем!\nХотите сыграть еще раз ?\n'

try_input = 0
try_predict = 0
valid_maximal_number = 0
random_number = 0
valid_predict_number = 0


def start_game():
    print(welcome_phrase)
    try_input = 0
    while try_input < 4:
        maximal_number = input('Нужно ввести число больше 1\n')
        if is_valid(maximal_number):
            return int(maximal_number)
        else:
            print(invalid_input_phrase.format(3 - try_input))
            try_input += 1
        if try_input == 4:
            print(end_game_phrase)
            exit()


def randomer(max_number):
    return rd.randint(1, max_number)


def is_valid(user_input):
    return user_input.isdigit() and int(user_input) >= 1


def valid_number(valid_maximal_number):
    try_input = 0
    while try_input < 4:
        number = input('введите цифру от 1 до {}\n'.format(valid_maximal_number))
        if is_valid(number) and 1 <= int(number) <= valid_maximal_number:
            return int(number)
        else:
            print(invalid_predict_input_phrase.format(valid_maximal_number, 3 - try_input))
            try_input += 1
    if try_input == 4:
        print(end_game_phrase)
        exit()


def game():
    valid_maximal_number = start_game()
    random_number = randomer(valid_maximal_number)
    valid_predict_number = valid_number(valid_maximal_number)
    try_predict = 1
    while random_number != valid_predict_number:
        if valid_predict_number > random_number:
            print(over_number_phrase)
            valid_predict_number = valid_number(valid_maximal_number)
            try_predict += 1
        if valid_predict_number < random_number:
            print(below_number_phrase)
            valid_predict_number = valid_number(valid_maximal_number)
            try_predict += 1
        if valid_predict_number == random_number:
            print(win_game_phrase.format(try_predict))
            if input('Введите д если хотите сыграть еще раз\n') == 'д':
                game()
            else:
                print(end_game_phrase)
                exit()


game()