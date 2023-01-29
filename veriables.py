"""5000 + % 2"""
urunA = 5500
urunB = 6000
urunC = 7000
kdv = 0.2

print(urunA + (urunA * kdv))
print(urunB + (urunB * kdv))
print(urunC + (urunC * kdv))
"""değişkenler sayı ile başlamaz
-- değişkenler boşluk içermez
-- türkçe karakter içermemelidir
-- büyük küçük harf duyarlılığı vardır"""

"""-- büyük küçük harf duyarlılığı vardır"""
yas = 20
YAS = 30
print(yas)
print(YAS)

"""örnek= 
sayi@=40  YANLIŞ"""

a, b, c, = 10, 20, 30  # bu şekilde atama yapılabilri
print(a, b, c)

x = 1
print(type(x))
y = 1.5
print(type(y))

name="hüseyin"
print(type(name))

isStudent=True
isStudent=False

print(type(isStudent))

x, y, name, isStudent=1, 1.5, "hüseyin", False
