n = int(input())
last_digit = n % 10

if last_digit % 2 == 0:
    for sum_digit in range(1, n):
        if sum_digit % 3 == 0:
            print(f"Число {n} делится на 6")
            
else:
    print(f"Число {n} не делится на 6")