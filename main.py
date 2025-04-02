import tic_tac_toe
import wheel_of_fortune
import two_players_tic

s = input('В какую игру поиграем ?\n1)Поле чудес = 1\n2)Крестики-нолики = 2\n'
          '3) Кресити-нолики на 2 Игрока = 3\n'
          '\tписать тут:')
if s == '1':
    wheel_of_fortune.game()
elif s == '2':
    tic_tac_toe.game()
elif s == '3':
    two_players_tic.game()
else:
    print('Не то ввел. Пока !!!')
