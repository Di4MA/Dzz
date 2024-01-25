amount, hour = int(input()), int(input())

if hour > 10 and hour < 12:
    amount /= 2
elif hour > 20 and hour < 22:
    amount /= 4

print(amount)