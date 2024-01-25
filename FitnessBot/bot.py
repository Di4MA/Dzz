import telebot
from telebot import types
import random
bot = telebot.TeleBot('6690402403:AAHSObV4o27IXY7L4ME5U7ZC9lo0OJ-uKk0')
k = 0
z = 0
x = 0
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
    #bot.reply_to(message,"Здравствуй, {0.first_name}\nСмотрю, вы заинтересовались нашим Фитнес клубом".format(message.from_user), parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['start'])

def privet(message): #поболтать, спросить
    while True:
        if "/start" in message.text:
            bot.send_message(message.from_user.id, "Привет,\nЯ FitnessBot! Готов служить тебе.")
            bot.register_next_step_handler(message, privet)
            break
        if "ривет" in message.text or "дравст" in message.text or "даров" in message.text or "хай" in message.text or "уден" in message.text or "/start" in message.text:
            bot.send_message(message.from_user.id, "Привет,\nЯ FitnessBot! Готов служить тебе.")
            bot.send_message(message.from_user.id,"Чем я могу тебе помочь?")
            break
        if "ак дел" in message.text or "какдел" in message.text or "Как дела" in message.text:
            bot.send_message(message.from_user.id, "Все отлично! Я очень счастлив помогать вам. Пишите мне почаще!")
            break
        if "деб" in message.text or "дау" in message.text or "дура" in message.text or "кака" in message.text or "бяк" in message.text or "туп" in message.text or "лох" in message.text:
            bot.send_message(message.from_user.id, "Кто обзывается, тот сам так называется!")
            break
        if "тзыв" in message.text or "/otzovi" in message.text:
            bot.send_message(message.from_user.id,"Здесь, вы сможете ознакомиться с отзывами реальных людей о Fitness Sirius: ")
            bot.send_message(message.from_user.id,"https://yandex.ru/maps/?ll=39.951073%2C43.414586&mode=poi&poi%5Bpoint%5D=39.950750%2C43.414516&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D49930719477&tab=reviews&z=16")
            break
        if "дрес" in message.text or "где" in message.text or "куда" in message.text or "/address" in message.text:
            bot.send_message(message.from_user.id, "Мы находимся по адресу: пгт Сирус, ул. Олимпийская, 1")
            break
        if "оборуд" in message.text or "тренаж" in message.text or "снари" in message.text or "/oboryd" in message.text:
            bot.send_message(message.from_user.id, "У нас есть:\n*Кардиотренажеры:*\n(орбитреки, беговые дорожки, велотренажеры, степпер, климбер)\n*Силовые тренажеры:*\n(рычажные, блочные) \n", parse_mode='Markdown')
            break
        if "какие" in message.text or "секци" in message.text or "занят" in message.text or "/kryjki" in message.text or "ружки" in message.text:
            bot.send_message(message.from_user.id, "Спортзал, Йога, Дзюдо (до 18 лет)")
            break
        if "асы" in message.text or "ремя раб" in message.text or "/chas" in message.text or "когда" in message.text or 'Когда' in message.text:
            bot.send_message(message.from_user.id, "*ПН-ПТ:* с 6:00 до 23:00\n*СБ-ВС:* с 6:00 до 22:00\n",parse_mode='Markdown')
            break
        if "апис" in message.text or "/zapic" in message.text:
            bot.send_message(message.from_user.id, "Вы хотите записаться?")
            bot.register_next_step_handler(message, get_b)
            break
        if "умеешь" in message.text or "меешь" in message.text:
            bot.send_message(message.from_user.id,"Я могу записать вас на занятие, подсказать какое у нас оборудование, адрес, показать отзывы, часы работы")
            break
        elif message.text == "/help":
            bot.send_message(message.from_user.id,"/help - *Помощь*\n/otzovi - *Отзывы о Fitness Sirius*\n/address - *Наш адрес*\n/oboryd - *Тренажеры*\n/kryjki - *Список занятий и секций*\n/chas - *Часы работы*\n/zapic - *Записаться онлайн*\n")
        else:
            bot.send_message(message.from_user.id, "Извини, я не совсем понимаю. Напиши /help.")
            break
        return
def get_b(message): #Выбор занятия
    while True:
        if "да" in message.text or "yes" in message.text:
            bot.send_message(message.from_user.id, "Выберите, на что хотите записаться")
            bot.send_message(message.from_user.id, "1 - Спортзал\n2 - Йога\n3 - Дзюдо (до 18 лет)")
            bot.register_next_step_handler(message, get_c)
            break
        if "no" in message.text or "нет" in message.text:
            bot.send_message(message.from_user.id, "Жаль, что вы передумали. Помните, что всегда можете одуматься и встать на истинный путь к успеху")
            break
        else:
            bot.send_message(message.from_user.id, "чего-чего?")
            bot.register_next_step_handler(message, privet)
            break

def get_c(message): #Выбор расписания
    while True:
        k = message.text
        if '1' in message.text or 'порт' in message.text or 'зал' in message.text or 'Зал' in message.text:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            but1 = types.KeyboardButton("запись")
            but2 = types.KeyboardButton("назад")
            markup.add(but1, but2)
            bot.send_message(message.from_user.id, " Вы выбрали Спортзал. Теперь выберите время")
            bot.register_next_step_handler(message, get_с1)
            break
        if '2' in message.text or 'йог' in message.text or 'Йог' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Йогу. Теперь выберите время")
            bot.send_message(message.from_user.id,"1. ПН - с 10:00 до 13:00\n2. ВТ - с 6:00 до 9:00\n3. СР - с 8:40 до 11:00\n4. ЧТ - с 10:00 до 13:00\n5. ПТ - с 10:00 до 13:00\n6. СБ - с 10:00 до 13:00\n7. ВС - с 8:00 до 11:00\n ")
            bot.send_message(message.from_user.id, "Выпишите цифру или цифры, на какие дни вас записать.")
            bot.register_next_step_handler(message, get_с2)
            break
        if '3' in message.text or 'Дзюд' in message.text or 'дзю' in message.text:
            bot.send_message(message.from_user.id, "Вы выбрали Дзюдо. Стоимость одного занятия составляет: 500₽\nТеперь выберите время")
            bot.send_message(message.from_user.id, "1. ПН - с 15:00 до 17:00\n2. ВТ - с 16:00 до 18:00\n3. СР - с 15:00 до 17:00\n4. ЧТ - с 14:30 до 16:00\n5. ПТ - с 15:00 до 17:00\n6. СБ - с 15:00 до 17:00\n7. ВС - с 11:00 до 13:00\n ")
            bot.send_message(message.from_user.id, "Выпишите цифру или цифры, на какие дни вас записать.")
            bot.register_next_step_handler(message, get_с3) # 1. 2. 3. 4. 5. 6. 7. выпишите  от 1 до 7 в какие дни будете ходить.
            break
        else:
            bot.send_message(message.from_user.id, "Попробуйте заново")
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
bot.polling(none_stop=True, interval=0)