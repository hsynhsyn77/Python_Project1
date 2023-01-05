import random

sayi = random.randint(1, 10)  # 1-100 arasında random sayı üretecek herseferinde farklı
can=int(input("kaç hak kullanmak istersiniz: "))
hak = can
sayac=0

while hak > 0:
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin : "))

    if sayi == tahmin:
        print(f"Tebrikler bildiniz {sayac}. defada bildiniz. Toplam puanınınız: {100-(100/can)*(sayac-1)}")
        break
    elif sayi>tahmin:
        print("yukarı")
    else:
        print("aşağı")
    if hak==0:
        print(f"hakkınız bitti. tutulan sayı : {sayi}")
