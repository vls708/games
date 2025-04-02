import random
import os

data = ['книга', 'месяц', 'ручка', 'шарик', 'олень']
square = '\u25F0'
haert = '\u2764'

def game():
    answer = input('Хотите сыграть в игру?(да/нет): ')
    while answer.lower() == 'да':
        life = choose_lifes()
        word = choose_word()
        field = [square for _ in word]
        print_field(field, life)
        while True:
            user_symb = get_symb_or_word()
            os.system('cls')
            field, life = check_symb_or_word(field, user_symb, word, life)
            if life == 0:
                print('Проиграл =(')
                break
            elif ''.join(field) == word:
                print('ПОБЕДА !!!')
                break
        if len(data) > 0:
            answer = input('сыграем еще раз? (да/нет): ')
        else:
            print('Игра окончена !!!')
            break


def choose_lifes():
    s = input('Выберите уровень сложности:\n1) Легкий\n2) Средний\n3) Сложный\n')
    if s == '1':
        return 7
    elif s == '2':
        return 5
    elif s == '3':
        return
    else:
        print('Неверный ввод! Для легкого - 1, для среднего - 2, для сложного - 3')

def choose_word():
    word = random.choice(data)
    data.remove(word)
    return word

def get_symb_or_word():
    return input('Введите букву или напишите слово целиком: ')

def print_field(map, life):
    for el in map:
        print(el, end='|')
    print(f' {haert} x {life}')

def check_symb_or_word(field, user_w, current_word, life):
    if len(user_w) == 1 and user_w in current_word:
        print('Есть такая буква!')
        change_field(field, current_word, user_w)
    elif current_word == user_w:
        field = [s for s in current_word]
    elif 1 < len(user_w) < len(current_word):
        print('Ошибка !!! Нужно вводить слово целиком или одну букву')
        life -= 1
    else:
        print('Ошибка!!! неверная буква или слово')
        life -= 1
    print_field(field, life)
    return field, life


def change_field(field, current_word, user_symb):
    for i, ch in enumerate(current_word):
        if ch == user_symb:
            field[i] = user_symb
