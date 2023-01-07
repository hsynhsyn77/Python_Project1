"""
# class
class Person:
    pass

    # class attributes
    address = "no information"
    # constructor (yapıcı method)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print("init methodu çalıştı")
    # instance methods
    def intro(self):
        print("hello There I'm " + self.name)
    def calculateAge(self):
        return 2019 - self.year
# object (instance)
p1 = Person(name="ali", year=1990)
p2 = Person(name="kaan", year=1995)
# updating
p1.name = "ahmet"
p1.address = "konya"

# accessing object  attributes
print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()} address : {p1.address}')
print(f'adım: {p2.name} ve yaşım: {p1.calculateAge()} adress : {p2.address}')

p1.intro()

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

"""


class Circle:
    pi: 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)


c1 = Circle()  # yaricap = 1
c2 = Circle()

print(f"c1 : alan={c1.alan_hesapla()} çevre : {c1.cevre_hesapla()}")
print(f"c2 : alan={c2.alan_hesapla()} çevre : {c2.cevre_hesapla()}")
