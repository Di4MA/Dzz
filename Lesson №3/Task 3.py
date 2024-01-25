AUG = input('? :').lower()
answer = ''
if AUG == 'продукты':
    price = int(input('Цена : '))
    if price < 100:
        answer = ' Пирожки ??? :)'
    elif price > 100 and price < 500:
        answer = 'Орешки в шоколаде ?'
    else:
        answer = 'Фрукты? '
else:
    answer = 'Как насчет хозтоваров? '

print(answer)