bykvi = list("АВЕКМНОРСТУХ")
cifri = list('0123456789')
import random
def generator_bykv():
    nomer = random.choice(bykvi) + random.choice(cifri) + random.choice(cifri) + random.choice(cifri) + random.choice(bykvi) + random.choice(bykvi) + random.choice(cifri) + random.choice(cifri)
    return nomer
print(generator_bykv())