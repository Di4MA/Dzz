def reverse(n):
    return n[: :-1]

def palidrome(n):
    cir = reverse(n)
    if (n == cir):
        return True
    return False

n = input("слово")
value = palidrome(n)
print(value)