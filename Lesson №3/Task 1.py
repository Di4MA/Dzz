price = int(input('Сумма к оплате: '))
time = int(input('Текущий час(8-22): '))

if time == 10 or time == 11 or time == 12 :
    price = price / 2
elif time == 20 or time == 21 or time == 22:
    price = price / 4

print(price)