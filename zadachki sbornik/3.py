spisok = [1, 3, 4, 1, 4, 5, 7, 8, 20, 22, 5]
vse = []
for yagoda in spisok:
    if spisok.count(yagoda)>1:
        vse.append(yagoda)
print("Повторы:", vse)