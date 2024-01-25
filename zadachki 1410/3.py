def magic_date(date):
    list1 = date.split(".")
    if int(list1[0]) * int(list1[1]) == int(list1[2]) % 100:
        return "Magic Date"
    else:
        return "not magic guys"
print(magic_date("10.06.1960"))