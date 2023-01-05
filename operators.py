""""1-Atama operatörleri"""
x = 10
y = 20
z = 30
x, y, *z = 10, 20, 30, 40  # * işareti koyarsak listede olmayanı  ona aktar deriz
print(x, y, z)

x += 5  # x = x + 5
x -= 5
x *= 5
x /= 5
x %= 5
x //= 5
x **= 5

"""2-Karşılaştırma operatorleri"""
# x, y, z = 10, 20, 20
# sonuc = (x == y)
# print(sonuc)
# sonuc = (z == y)
# print(sonuc)
# sonuc = (z != y)
# print(sonuc)
# sonuc = (x > y)
# print(sonuc)
# sonuc = (x <= y)
# print(sonuc)

"""3-Mantıksal operatorler"""
# and
# or
# Not
sonuc1 = 5 < x < 15
sonuc2 = (x > 5)
sonuc3 = (x > 5)
print(sonuc1)
print(sonuc2)
print(sonuc3)

# b- or
""" mezuniyet en az lise ve yaş en az 18 olmalı"""

mezuniyet = "ilkokul"
yas = 20
sonuc4 = (mezuniyet == "ilkokul" or mezuniyet == "lise" or mezuniyet == "lisans") and (yas >= 18)
print(sonuc4)

# c - Not

sonuc = not (True)
sonuc = not (False)

#  identity operatörü

a = [1, 2, 3]
b = a
print(a is not b)

print(1 in a)

meyveler = ["elma", "armut"]
print("muz" in meyveler)
print("elma" in meyveler)
