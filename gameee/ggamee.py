print('\nОткрыв дверь, вы попадаете в маленькую комнату размером метр на метр. В этой комнате есть 3 двери.\nНа вид все они одинаковые, кроме их нумерации: (1, 2, 3) .')
print("═══════════════════════════════════════════════════════════════════════════════════\n"
      "══════════███████████████═════════███████████████═════════███████████████══════════\n"
      "══════════███████████████═════════███████████████═════════███████████████══════════\n"
      "══════════██████═══██████═════════████══════█████═════════████═══════████══════════\n"
      "══════════██████═══██████═════════███══████══████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════█████████══████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════████████══█████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════███████══██████═════════████═══════████══════════\n"
      "══════════██████═══██████═════════██████══███████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════█████══████████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════████══█████████═════════██████████═████══════════\n"
      "══════════██████═══██████═════════███═════════███═════════████═══════████══════════\n"
      "══════════███████████████═════════███████████████═════════███████████████══════════\n"
      "══════════███████████████═════════███████████████═════════███████████████══════════\n"
      "═══════════════════════════════════════════════════════════════════════════════════")

print("\nКакую дверь вы выберете?")
room = input()
if room not in ('1', '2', '3'):
    print("Вы решили не играть в игры Дьявола и просто вышли назад")
    exit(0)
elif room == '1':
    print('Вы зашли в 1 дверь, перед вами две двери, в какую вы пойдете?')
    door = input()
    if door not in ('1', '2'):
        print("О нет! Оказалось, что у вас была клаустрофобия.Вы сели схватившись за голову. Вы больше не выбиретесь от сюда.")
        exit(0)
    elif door == '1':
        print('Вы вышли из подземелья!')
    elif door == '2':
        print('Вы проволились в огромную яму и умерли с голода')
if room == '2':
    print('Вы пошли направо, перед вами две двери, в какую вы пойдете(введите номер двери)?')
    door = input()
    if door not in ('1', '2'):
        exit(0)
    elif door == '1':
        print('Вы нашли ультра редкий предмет ничего')
    elif door == '2':
        print('Вы нашли сокровища')
if room == '3':
    print('Вы пошли прямо, перед вами две двери, в какую вы пойдете(введите номер двери)')
    door = input()
    if door not in ('1', '2'):
        exit(0)
    elif door == '1':
        print('Перед вами две двери (1,4) какую выберите?')
        door = input()
        if door not in ('1', '2'):
            exit(0)
        elif door == '1':
            print('Вы нашли комнату с никогда не спящим существом по имени программист')
        elif door == '4':
            print('Вы вернулись в первую комнату с дверьми.')
    elif door == '2':
        print('Вы нашли комнату с человеком который сейчас сидит и пишет этот код')