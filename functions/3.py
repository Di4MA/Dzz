ycheniki = int(input("Введите количество учеников "))
def get():
    for i in range(ycheniki):
        print("Привет. Для зачета мне необходимо спросить у тебя пару вопросиков")
        bal = int(input("Какой у тебя бал"))
        if bal >= 50:
            print("Поздравляю! ВЫ допущены к зачету")
        else:
            print("ВЫ отчислены (не дай бог мне такое)")