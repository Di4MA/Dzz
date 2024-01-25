from time import time
start = time()
end = time()
zatrat = None
def game():
    while start - end < 1800:
        xod = input("Куда сходите? ")
        if xod == "off":
            break
        zatrat = 0
        zatrat = time() - start
        print("Вы потратили на ход:", round(zatrat),"с")
        zatrat_all = (start-time()+1800) / 60
        print("всего осталось", round(zatrat_all), "мин.")
game()