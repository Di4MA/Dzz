class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age
    def change_rating(self, value):
        if value > 0:
            if self.rating + value <= 100:
                self.rating += value
            if self.age > 18:
                self.age -= abs(value)//10
            else:
                self.rating = 100
        elif value < 0:
            if self.rating + value >= 1:
                self.rating += value
                self.age -= abs(value)//10
            else:
                self.rating = 1
    def __iadd__(self, string):
        self.rating += len(string)
        if self.age - len(string) //10 >18:
            self.age -= len(string)//10
        return self
    def __call__(str, number):
        return (number - self.age) * self.rating
    def __str__(self):
        return "Wizard{self.name} with {self.rating} rating looks {self.age} years old"
    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age != other.age:
            return self.age < other.age
        else:
            return self.name < other.name
    def __le__(self, other):
        return self < other or self == other
    def __ge__(self, other):
        return self > other or self == other
    def __eq__(self, other):
        return self.name == other.name and self.rating == other.rating and self.age == other.age
    def __ne__(self, other):
        return not self.__eq__(other)
