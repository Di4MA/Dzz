
class Pin:
    def init(self, a, b):
        self.a = a
        self.b = b

    def outer_circle(self):
        r = ((self.a2 + self.b2) ** 0.5 / 2)
        return r

class Hole:
    def init(self, r):
        self.r = r

    def is_fit(self, pin):
        if pin.outer_circle() <= self.r:
            return True
        else:
            return False

# Создаем отверстие и штыри
hole = Hole(10, 2)
pin1 = Pin(3, 4)
pin2 = Pin(2, 2)
pin3 = Pin(6, 8)

# Проверяем работоспособность
print(hole.is_fit(pin1))  # True
print(hole.is_fit(pin2))  # True
print(hole.is_fit(pin3))  # False