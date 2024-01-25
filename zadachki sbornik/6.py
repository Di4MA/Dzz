days = [ "Пн", "Вт", "Ср", "Пт", "Сб", "Вс"]
week = {}
for day in days:
    week[day] = days.index(day) + 1
    print(week)