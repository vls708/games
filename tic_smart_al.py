import random
import time

maps = [i for i in range(1, 10)]

victories = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

def print_maps():
    print('-' * 13)
    for i in range(3):
        print(f'| {maps[0 + i * 3]} | {maps[1 + i * 3]} | {maps[2 + i * 3]} |')
        print('-' * 13)

def step_in_map(n, symbol):
    ind = maps.index(n)
    maps[ind] = symbol

def ai_step():
    data = [el for el in maps if el != 'X' and el != '0']
    return random.choice(data)

def get_result():
    s = ''
    for line in victories:
        if maps[line[0]] == 'X' and maps[line[1]] == 'X' and maps[line[2]] == 'X':
            s = 'X'
        if maps[line[0]] == '0' and maps[line[1]] == '0' and maps[line[2]] == '0':
            s = '0'
    return s


def game():
    name = input('Введите ваше имя: ')
    is_human = True
    count = 0
    while True:
        count += 1
        print_maps()
        if is_human:
            number = input(f'Ваш ход, {name}: ')
            step_in_map(int(number), 'X')
            is_human = False
        else:
            print('Ход компьютера!!!')
            time.sleep(1)
            number = ai_step()
            step_in_map(int(number), '0')
            is_human = True
        win = get_result()
        if win == 'X':
            print(f'{name} победил!!!')
            break
        elif win == '0':
            print(f'Компьютер победил!!!')
            break
        if count == 9:
            print('Ничья \м/')
            break

