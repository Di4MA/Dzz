print("Привет! Вижу, что ты заинтересовался/(лась) нашим Фитнес Клуб 'Di4ma'. Хочешь узнать что-то про Фитенес клуб (например: рассписание тренировок или стоимость абонементов)?")

k = 0
z = 0
x = 0

def privet(message): #поболтать, спросить
    while True:
        if "/start" in message:
            print("Привет,\nЯ FitnessBot! Готов служить тебе.")
        if "ривет" in message or "дравст" in message or "даров" in message or "хай" in message or "уден" in message or "/start" in message:
            print("Привет,\nЯ FitnessBot! Готов служить тебе.")
            print("Чем я могу тебе помочь?")
        if "ак дел" in message or "какдел" in message or "Как дела" in message:
            print("Все отлично! Я очень счастлив помогать вам. Пишите мне почаще!")
        if "деб" in message or "дау" in message or "дура" in message or "кака" in message or "бяк" in message or "туп" in message or "лох" in message:
            print("Кто обзывается, тот сам так называется!")
            break
        if "тзыв" in message or "/otzovi" in message:
            print("Здесь, вы сможете ознакомиться с отзывами реальных людей о Fitness Sirius: ")
            print("https://yandex.ru/maps/?ll=39.951073%2C43.414586&mode=poi&poi%5Bpoint%5D=39.950750%2C43.414516&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D49930719477&tab=reviews&z=16")
            break
        if "дрес" in message or "где" in message or "куда" in message or "/address" in message:
            print("Мы находимся по адресу: пгт Сирус, ул. Олимпийская, 1")
            break
        if "оборуд" in message or "тренаж" in message or "снари" in message or "/oboryd" in message:
            print("У нас есть:\n*Кардиотренажеры:*\n(орбитреки, беговые дорожки, велотренажеры, степпер, климбер)\n*Силовые тренажеры:*\n(рычажные, блочные) \n")
            break
        if "какие" in message or "секци" in message or "занят" in message or "/kryjki" in message or "ружки" in message:
            print("Спортзал, Йога, Дзюдо (до 18 лет)")
            break
        if "асы" in message or "ремя раб" in message or "/chas" in message or "когда" in message or 'Когда' in message:
            print("*ПН-ПТ:* с 6:00 до 23:00\n*СБ-ВС:* с 6:00 до 22:00\n")
            break
        if "апис" in message or "/zapic" in message:
            print("Вы хотите записаться?")
            if "да" in message or "yes" in message:
                print("Выберите, на что хотите записаться")
                print("1 - Спортзал\n2 - Йога\n3 - Дзюдо (до 18 лет)")
                break
            if "no" in message or "нет" in message:
                print("Жаль, что вы передумали. Помните, что всегда можете одуматься и встать на истинный путь к успеху")
                break
            else:
                print("чего-чего?")
                break

                print("ok")
            break
        if "умеешь" in message or "меешь" in message:
            print("Я могу записать вас на занятие, подсказать какое у нас оборудование, адрес, показать отзывы, часы работы")
            break
        elif message == "/help":
            print("/help - *Помощь*\n/otzovi - *Отзывы о Fitness Sirius*\n/address - *Наш адрес*\n/oboryd - *Тренажеры*\n/kryjki - *Список занятий и секций*\n/chas - *Часы работы*\n/zapic - *Записаться онлайн*\n")
        else:
            print("Извини, я не совсем понимаю. Напиши /help.")
            break
        return
        message = input("Что интересует")

def get_c(message): #Выбор расписания
    while True:
        k = message
        if '1' in message or 'порт' in message or 'зал' in message or 'Зал' in message:
            print(" Вы выбрали Спортзал. Теперь выберите время")
            break
        if '2' in message or 'йог' in message or 'Йог' in message:
            print("Вы выбрали Йогу. Теперь выберите время")
            print("1. ПН - с 10:00 до 13:00\n2. ВТ - с 6:00 до 9:00\n3. СР - с 8:40 до 11:00\n4. ЧТ - с 10:00 до 13:00\n5. ПТ - с 10:00 до 13:00\n6. СБ - с 10:00 до 13:00\n7. ВС - с 8:00 до 11:00\n ")
            print("Выпишите цифру или цифры, на какие дни вас записать.")
            break
        if '3' in message or 'Дзюд' in message or 'дзю' in message:
            print("Вы выбрали Дзюдо. Стоимость одного занятия составляет: 500₽\nТеперь выберите время")
            print("1. ПН - с 15:00 до 17:00\n2. ВТ - с 16:00 до 18:00\n3. СР - с 15:00 до 17:00\n4. ЧТ - с 14:30 до 16:00\n5. ПТ - с 15:00 до 17:00\n6. СБ - с 15:00 до 17:00\n7. ВС - с 11:00 до 13:00\n ")
            print("Выпишите цифру или цифры, на какие дни вас записать.")
            bot.register_next_step_handler(message, get_с3) # 1. 2. 3. 4. 5. 6. 7. выпишите  от 1 до 7 в какие дни будете ходить.
            break
        else:
            print("Попробуйте заново")
            break

cpicok_day = (" ")#типо это список и сюда можно добавлять, наверное, я пытался немного не получилось, бот в тг сложный какойто и не понятный если честно
def get_с3(message): # свое имя. в идеале это все добавлять в список и потом его выводить но я устал если честно
    while True:

        if '1' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Понедельник 15:00 - 17:00.")
            bot.register_next_step_handler(message, konec_zapic)

        if '2' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Вторник 16:00 - 18:00.")
            bot.register_next_step_handler(message, konec_zapic)

        if '3' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Среда 15:00 - 17:00." )
            bot.register_next_step_handler(message, konec_zapic)

        if '4' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Четверг 14:30 - 16:00.")

            bot.send_message(message.from_user.id, "На чьё Имя хотите записаться?")
            bot.register_next_step_handler(message, konec_zapic)
            break
        if '5' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Пятница 15:00 - 17:00.")
            bot.register_next_step_handler(message, get_с3)
            break
        if '6' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Суббота 15:00 - 17:00.")
            bot.register_next_step_handler(message, get_с3)
            break
        if '7' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Воскресенье 11:00 - 13:00.")
            bot.register_next_step_handler(message, get_с3)
            break
       # else:
        #    bot.send_message(message.from_user.id, "Введите только цифры, которые относятся к записи: (1,2,3,4,5,6,7)")
         #   bot.register_next_step_handler(message, get_c)
          #  break забагалась плчемуто

def konec_zapic(message): #вывод итога Кто куда когда записался
    while True:
        bot.send_message(message.from_user.id, "Спасибо! Я записал Вас. С нетерпением будем вас ждать")
        bot.register_next_step_handler(message, privet)
        break
