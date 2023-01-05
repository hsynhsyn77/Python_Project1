urunler = ["samsung s20", "samsung s21", "samsung s22"]

# ekleme
urunler.append("ıphone 11")
print(urunler)
urunler.insert(1, "ıphone x")
print(urunler)
urunler.insert(-1, "ıphone 12")
print(urunler)
urunler.insert(len(urunler), "ıphone 13")
print(urunler)

# silme
urunler.remove("samsung s20")
print(urunler)
urunler.pop()  # listenin en sonuncu elemanı siler
print(urunler)
# del urunler
del urunler[0]
print(urunler)

# urunler.clear()
# print(urunler)

urunler2 = urunler
print(urunler)
print(urunler2)

urunler[0] = "değiştir"
print(urunler)

urunler2[0] = "değiştir"
print(urunler2)

urunler2 = urunler.copy()
print(urunler2)

urunler.extend(urunler)
print(urunler)

fiyatlar = [5000, 4000, 2000]
sonuc = min(fiyatlar)
print(sonuc)
sonuc = max(fiyatlar)
print(sonuc)
sonuc = min(urunler)
sonuc = max(urunler)
fiyatlar.sort()
urunler.sort()
print(sonuc)
print(urunler)

sonuc = urunler.count("samsung s22")
print(sonuc)

isimler =[]

isim=input("isim: ")
isimler.append(isim)

isim=input("isim: ")
isimler.append(isim)

isim=input("isim: ")
isimler.append(isimler)

print(isimler)
