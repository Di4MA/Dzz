add_new = input('Хотите добавить нового преподавателя? y - если да, n - если хотите завершить программу ')
list = []
while add_new !='n':
    surname = input('ведите фамилию преподавтателя: ')
    job = input('Введите должность преподавателя: ')
    amount = input('ведите общие число студентов ').split(',')
    list.append ([surname , job,amount])
    add_new= input('Хотите добавить нового преподавателя ? y - да n -нет ')
    print(list)