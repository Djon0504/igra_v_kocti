import random
import time

def dice():
    player = random.randint(1, 6)
    print("У вас выполо" + str(player))

    ai = random.randint(1, 6)
    print('Компьютер делает бросок...')
    time.sleep(2)
    print('У компьютера выпало' + str(ai))

    if player > ai:
        print("Вы победили")
    else:
        print("Вы проиграли")

    print("Выход? Y/N")
    resume = input()

    if resume == 'Y' or resume == 'y':
        exit()
    elif resume == 'N' or resume == 'n':
        pass
    else:
        print('Ваш выбор непонятен. Сыграйте еще раз?')

#Главный цикл
while True:
    print("Нажимайте кнопку вода, чтобы бросить кубик")
    poll = input()
    dice()
