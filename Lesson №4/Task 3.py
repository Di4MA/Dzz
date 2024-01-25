login = input("Введите ваш логин: ")
spisok_kakashek = ['=', '?', '^', '$', '№', '@', '_', '~', "'", "(", ")", ",", "*", "%"]
for letter in login:
    if letter in spisok_kakashek:
        print("Логин не корректный. Символ ", letter, "запрещен")
        break

else: print (input("Введите пароль: "))