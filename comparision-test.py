# 1- girilen 2 sayıdan hangisi büyüktür
a = int(input("sayı1: "))
b = int(input("sayı2: "))
result = (a > b)
print(f'a:{a} b:{b} den büyüktür:{result}')

# 2- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalma hesaplayınız
#   eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazın

vize1 = float(input("1.vize: "))
vize2 = float(input("2.vize: "))
final = float(input("final: "))
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f'not ortalamanız: {ortalama} ve dersden geçme durumunuz {ortalama >= 50}')

# 3- girilen bir sayının tek mi çift mi olduğunu yazdırınız

sayi = int(input("sayı: "))
tekCift = (sayi % 2 == 0)
print(f'girilen sayı çift olma durumu:{tekCift}')

# 4- girilen bir sayının negatif pozitif durumunu yazdırın

sayi = int(input("sayı: "))
pozitifmi = (sayi > 0)
print(f'girilen sayının pozitif olma durumu {pozitifmi}')
# 5- parola ve email bilgisini isteyip doğruluğunu kontrol ediniz

email = "email@huseyinsirikci.com"
password = "abc123"
girilenEmail = input("email: ")
girilenPassword = input("parola: ")

isEmail=(email==girilenEmail.lower().strip())#mail i yazdıkdan sonra boşluk bırakırsak da kabul etsin diye strip methodu kullandık
# lower methodu ile büyük küçük harf kabul görmesi içim
isPassword=(password==girilenPassword.lower())
print(f'Email bilgisi doğrumu: {isEmail} ve parola bilgisi doğrumu: {isPassword}')

#   (email: email@huseyinsirikci.com  parola: abc123)
