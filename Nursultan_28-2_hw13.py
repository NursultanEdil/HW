pip install python-decouple
import random
from decouple import config

# settings.py
MY_MONEY = int(config("MY_MONEY", default="1000"))

# logic.py
def get_result(money, start_money):
    if money > start_money:
        return f"Поздравляем! Вы выиграли {money - start_money}$"
    elif money < start_money:
        return f"Вы проиграли {start_money - money}$"
    else:
        return "Вы закончили игру с тем же количеством денег, что и начали"

# game.py
money = MY_MONEY
slots = list(range(1, 31))

print(f"У вас {money}$ на счету")

while True:
    slot = int(input("На какой слот поставить деньги? (1-30): "))
    if slot not in slots:
        print("Неверный номер слота")
        continue
    bet = int(input(f"Сколько поставить на слот {slot}? "))
    if bet > money:
        print("У вас недостаточно денег")
        continue
    win_slot = random.choice(slots)
    if slot == win_slot:
        win_amount = bet * 2
        money += win_amount
        print(f"Поздравляем! Вы выиграли {win_amount}$")
    else:
        money -= bet
        print(f"Вы проиграли {bet}$")
    print(f"У вас осталось {money}$")
    if money <= 0:
        print("У вас закончились деньги")
        break
    play_again = input("Хотите сыграть еще? (y/n) ")
    if play_again.lower() != "y":
        break

result = get_result(money, MY_MONEY)
print(result)
