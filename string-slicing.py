ad = "Hüseyin"
soyad = "ŞİRİKÇİ"
yas = "44"

msj = "Benim adım " + ad + " ve soyadım " + soyad + ".Yaşım ise " + yas + " ."

karakterUzunluk = len(msj)

print(msj)
"""ilk karakteri verir"""
print(msj[0])  # B
"""son karakteri verir"""
print(msj[-1])  # .
print(msj[-3])  # 4

print(msj[0:5])  # Benim
print(msj[0:7])  # Benim a
print(msj[0:7:2])
print(msj[6:16])
print(msj[:16])
print(msj[6:])
print(msj[-3:-1])  # son karakteri almaz
print(msj[-3:])  # son karaktere kadar alır
print(msj[-30:-10])
print(msj[::1])
print(msj[::-1])  # tersden yazar
print(msj[karakterUzunluk - 1])  # .
print(karakterUzunluk)
