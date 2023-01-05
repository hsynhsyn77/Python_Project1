"""sayi1 = int(input("sayı1 : "))
if (sayi1 > 0) and (sayi1 <= 100):
    print("sayı 0-100 arasında")
else:
    print("sayı 0-100 arasında değil")


sayi2 = int(input("sayı2 : "))
if (sayi2 > 0):
    if (sayi2 % 2 == 0):
        print("sayı pozitif çift sayıdır")
    else:
        print("sayı pozitif ancak sayı tek tir")
else:
    print("sayı negatiftir")


email = "email@hüseyin.com"
password = "abc123"

girilenEmail = input("email : ")
girilenPassword = input("password : ")

if (girilenEmail == email):
    if (girilenPassword == password):
        print("uygulamaya giriş başarılı")
    else:
        print("parolanız yanlış")
else:
    print("email bilginiz yanlış")


a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
if (a > b) and (a > c):
    print("a enbüyük sayıdır")
elif (b > a) and (b > c):
    print("b enbüyük sayıdır")
elif (c > a) and (c > b):
    print("c enbüyük sayıdır")

"""

# vize1 = float(input("vize1 : "))
# vize2 = float(input("vize2 : "))
# final = float(input("final : "))
##
#ortalama = ((vize1 + vize2) / 2) * 0.6 + (final * 0.4)
# if (ortalama>=50):
#    if(final >= 50):
#        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
#    else:
#        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız en az 50 almalısınız')
# else:
#    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

# if(ortalama<=50):
#    print(f"{ortalama} başarılı")
# else:
#    if(final>=70):
#        print(f"{ortalama} finalden en az 70 aldığınız için başarılı")
#    else:
#        print(f"{ortalama} başarısız")

name = input("adınız : ")
kg = float(input("kilonuz : "))
hg = float(input("boyunuz : "))

index = (kg) / (hg ** 2)

if(index>=0) and (index<=18.4):
    print(f"{name} kilo endexiniz {index} ve kilo değerlendirmen zayıf")
elif(index>18.4) and (index<=24.9):
    print(f"{name} kilo endexiniz {index} ve kilo değerlendirmen normal")
elif (index > 24.9) and (index <= 29.9):
    print(f"{name} kilo endexiniz {index} ve kilo değerlendirmen kilolu")
elif (index > 29.9) and (index <= 34.9):
    print(f"{name} kilo endexiniz {index} ve kilo değerlendirmen obez")
else:
    print("bilgileriniz yanlış")




