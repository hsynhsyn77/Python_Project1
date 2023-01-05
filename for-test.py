sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

for sayi in sayilar:
    if (sayi % 3 == 0):
        print(sayi)
# sayıların toplamı
toplam = 0
for sayi in sayilar:
    toplam += sayi
print("toplam:", toplam)
# tek sayıların karesi
for sayi in sayilar:
    if (sayi % 2 == 1):
        print(sayi ** 2)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "maraş"]

for sehir in sehirler:
    if (len (sehir) <= 5):
        print(sehir)

    urunler =[
    {"name": "samsung s6", "price": "3000"},
    {"name": "samsung s7", "price": "4000"},
    {"name": "samsung s8", "price": "5000"},
    {"name": "samsung s9", "price": "6000"},
    {"name": "samsung s10", "price": "7000"}
]
toplam=0
for urun in urunler:
    fiyat=int(urun["price"])
    toplam+=fiyat
print("toplam ürün fiyatı : ", toplam)

for urun in urunler:
    if (int(urun["price"])<=5000):
        print(urun)
