listgames=[]
game = input('Название игры ')
while game !='0':
    if game in listgames:
        print('Эта игра уже записана')
    else:
        listgames.append(game)
    game = input('Название игры ')
listgames.sort()
print(listgames)