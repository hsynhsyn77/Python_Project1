isim = "çınar"
isim2 = "ali"
isim20 = "hüseyin"

isimler = ["çınar", "ali", "hüseyin"]
print(isimler[0])
print(isimler[1])
print(isimler[2])

# list, tuple, set, dictionary

# list => sıralanabilir, değiştirilebilir, tekrarlanabilir

notlar = [70, 80, 50]

print(f"{isimler[0]} isimli öğrencinin notu: {notlar[0]}")
print(f"{isimler[1]} isimli öğrencinin notu: {notlar[1]}")
print(f"{isimler[2]} isimli öğrencinin notu: {notlar[2]}")

ogrenci1 = ["çınar", 70]
ogrenci2 = ["ali", 80]
ogrenci3 = ["hüseyin", 50]

#nesded list=> içiçe liste
ogrenciler = [
    ["çınar", 70],
    ["ali", 80],
    ["hüseyin", 50]
]
print(ogrenciler[0][0])
print(ogrenciler[0][1])

markalar=["mazda", "opel","toyota","bmw"]

sonuc=markalar[0:3]
print(sonuc)
sonuc=markalar[:3]
print(sonuc)
sonuc=markalar[1:]
print(sonuc)
sonuc=markalar[::-1]
print(sonuc)

# değiştirme
markalar[0:1]=["citroen","audi","honda"]
print(markalar)
markalar[0:2]=["citroen","audi","honda"]
print(markalar)
markalar[0:3]=["citroen","audi","honda"]
print(markalar)
userA="kaan",8
userB="simay",15
users=[userA,userB]
print(users)
print(users[1][0])
print(users[0][0])
