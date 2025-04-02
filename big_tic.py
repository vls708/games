import random
import time

maps = [i for i in range(1, 17)]

victories = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11),
    (12, 13, 14, 15),
    (0, 4, 8, 12),
    (1, 5, 9, 13),
    (2, 6, 10, 11),
    (3, 7, 11, 15),
    (0, 5, 10, 15),
    (3, 6, 9, 12),
  )

def print_maps():
    print('-' * 19)
    for i in range(4):
        print(f'| {maps[0 + i * 4]:2} | {maps[1 + i * 4]:2} | {maps[2 + i * 4]:2} | {maps[3 + i * 4]:2}')
        print('-' * 19)

def step_in_map(n, symbol):
    ind = maps.index(n)
    maps[ind] = symbol


# def ai_step():
#     data = [el for el in maps if el != 'X' and el != '0']
#     return random.choice(data)

def get_result():
    s = ''
    for line in victories:
        if maps[line[0]] == 'X' and maps[line[1]] == 'X' and maps[line[2]] == 'X' and maps[line[3]] == 'X':
            s = 'X'
        if maps[line[0]] == '0' and maps[line[1]] == '0' and maps[line[2]] == '0' and maps[line[3]] == '0':
            s = '0'
    return s



def game():

    name1 = input('Введите ваше имя: ')
    name2 = input('Введите ваше имя: ')
    is_human1 = True
    is_human2 = True
    count = 0
    while True:
        count += 1
        print_maps()
        if is_human1:
            number = input(f'Ваш ход, {name1}: ')
            step_in_map(int(number), 'X')
            is_human1 = False
        else:
            print(f'Ход, {name2}!!!')
            number = input(f'Ваш ход, {name2}: ')
            step_in_map(int(number), '0')
            is_human2 = False
            is_human1 = True
        win = get_result()
        if win == 'X':
            print(f'{name1} победил!!!')
            break
        elif win == '0':
            print(f'{name2} победил!!!')
            break
        if count == 15:
            print('Ничья \м/')
            break

game()