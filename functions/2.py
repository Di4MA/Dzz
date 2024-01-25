bal = int(input("Введите ваш бал"))
k = 0
p = "НУ ЕСЛИ ЧЕСТНО Я НЕМНОГО СХИТРИЛ, ПРИЗНАЮСЬ. НО А КАК ИСПОЛЬЗОВАТЬ ЭТИ ВАШИ ФУНКЦИИ DEF????"
if bal <= 49:
    k = 1
if bal >= 50 and bal <= 99:
    k = 2
if bal >= 100:
    k = 3

def discount():
    if k == 1:
        print("Ваш бал:", bal, "УРА!! ваша скидка составиляет 10%")
    return k

def discount():
    if k == 2:
        print("Ваш бал:", bal, "УРА!! ваша скидка составиляет 15%")
    return k

def discount():
    if k == 3:
        return k
print("Ваш бал:", bal, "УРА!! ваша скидка составиляет 20%")