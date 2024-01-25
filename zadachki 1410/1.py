import random
def password_gener(n):
    sym = list("1234567890qwertyuiop[]\|/asdfghjkl;:zxcvbnm,./!@$%^&*()_+~")
    password = ""
    for i in range(n):
        password += sym[random.randint(0,len(sym))]
    return password

n = int(input("Введите количество символов в пароле"))
print(password_gener(n))