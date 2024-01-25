marks = []
a = [5,4,3,2]
while 1:
    mark = (input("Введите ваши оценки через пробел").split())
    if mark == 0 : break
    elif mark in a :
        marks.append(mark)
    else: print('error')

print((len(marks) - marks.count(2))/len(marks)*100)