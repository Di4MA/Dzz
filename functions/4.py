ves = int(input("Введите ваш вес "))
rost = int(input("Введите ваш рост "))
def IMT_chet(ves, rost):
    IMT = (ves / (rost / 100) **2)
    return IMT

def IMT_obrabotka(ves, rost):
    IMT_result = IMT_chet(ves, rost)
    if IMT_result <= 18.5:
        print("Недостаточной вес")
    elif IMT_result >= 18.5 and IMT_result <= 25:
        print("Ваш индекс массы тела в норме. ВСЕ ОК")
    elif IMT_result >= 25:
        print("Избыточный вес")
