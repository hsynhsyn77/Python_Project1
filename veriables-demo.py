"""
->değişkenler  rakam ile başlayamaz
->büyük küçük harf duyarlılığı vardır
->türkçe karakter kullanmamalıyız

Uygulama 1 : bir öğrencinin aşağıdaki bilgileri için gerekli değişkenleri oluşturunuz.
Öğrenci adı
Öğrenci soyadı
Öğrenci ad + soyad
Öğrenci numarası
Öğrenci cinsiyet
Öğrenci TC kimlik
Öğrenci doğum yılı
Öğrenci adres bilgisi
Öğrenci yaşı
"""
ogrenciAdi = "hüseyin"
ogrenciSoyad = "şirikçi"
ogrenciAdSoyad = ogrenciAdi + " " + ogrenciSoyad
print(ogrenciAdSoyad)

ogrenciCinsiyet = True  # Erkek
print(ogrenciCinsiyet)

ogrenciCinsiyet = False  # Kadın
print(ogrenciCinsiyet)
ogrenciTckimlik = "123456789100"
ogrenciDogumYili = 1978

ogrenciYas = 2022 - ogrenciDogumYili
print(ogrenciYas)

ogrenciAdres = "Konya Selçuklu"
"""
Uygulama 2: Aiağıdaki ürünlerin toplam bilgisini hesaplayınız

Ürün 1 => 50  TL
Ürün 2 => 60.5 TL
Ürün 3 => 356.45 Tl

"""

urun1 = 50
urun2 = 60.5
urun3 = 356.45

toplam =urun1+urun2+urun3
print("ürün toplamı:", toplam)
