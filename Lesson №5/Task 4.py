result = {}
music = input ("Введите данные в виде (место в чарте, исполнитель, название)").lower()
while music != "off":
    new_music = music.split(",")
    result[(new_music[0],new_music[1])] = new_music[2]
    music = input ("Введите данные в виде (место в чарте, исполнитель, название)"). lower()
print (result)