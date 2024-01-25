Product1 = int(input("Цена первого товара:" ))
Product2 = int(input("Цена второго товара:" ))
Product3 = int(input("Цена третього товара:" ))
sym = Product1 + Product2 + Product3
if Product3 > Product1 and Product2 > Product1:
    print ("Акция! к оплате: ", Product3 / 2)
elif Product3 > Product2 and Product2 > Product1:
    print ("Акция! к оплате: ", sym/ 3)
else:
    print ("Акция! ой... увы, но для вас нет никаких акции", "К оплате: ", sym)