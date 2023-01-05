# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

sayi = float(input("sayı gir: "))
result = (sayi > 0) and (sayi <= 100)
print(f'sayı 0 ile 100 arasındamı : {result}')

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

sayi = int(input("sayı gir: "))
result = (sayi > 0) and (sayi % 2 == 0)
print(f"girilen sayı pozitif ve çift mi : {result}")

# 3- email ve parola bilgileri ile giriş kontroolü yapınız

email = "email@huseyin.com"
password = "abc123"

girilenEmail = input("email: ")
girilenPassword = input("password: ")
result = (girilenEmail == email) and (girilenPassword == password)
print(f'uygulamaya giriş başarılı mı : {result}')

# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
result = (a > b) and (a > c)
print(f'a en büyük sayıdır : {result}')

result = (b > a) and (b > c)
print(f'b en büyük sayıdır : {result}')

result = (c > b) and (c > a)
print(f'c en büyük sayıdır : {result}')

# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınızz
#   eğer ortalama 50 ve üstündüyse geçti değilse kaldı yazdırınız
vize1 = float(input("vize 1 : "))
vize2 = float(input("vize 2 : "))
final = float(input("final : "))

ortalama = (vize1 + vize2) / 2 * 0.6 + (final * 0.4)
result = (ortalama >= 50) and (final >= 50)

print(f'öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}')

#   a) ortalama 50 olsa bile final notu en az 50 olmalıdır

#   b) finalden 70 alındığında ortalamanın önemi olmasın

# 6- kişinin ad, k,lo ve boy bilgilerini alıp k,lo indekslerini hesaplayınız
#   Formül : ;(kilo / boy uzunluğunun karesi)

name = input("adınız : ")
kg = float(input("kilonuz : "))
hg = int(input("boyunuz : "))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)

print(f'{name} kilo endeksin : {index} ve kilo değerlendirmen zayıf : {zayif}')
print(f'{name} kilo endeksin : {index} ve kilo değerlendirmen normal : {normal}')
print(f'{name} kilo endeksin : {index} ve kilo değerlendirmen kilolu : {kilolu}')
print(f'{name} kilo endeksin : {index} ve kilo değerlendirmen obez : {obez}')
