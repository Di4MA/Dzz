str1 = ")()()()()())"

index_open = str1.find("(")
index_close = str1.rfind(")")

if index_close < index_open:
    print ("Валидных скобочек нет")
else:
    print (index_close - index_open)