sayi1 = 30
sayi2 = 30
kosul = (sayi1 > sayi2)

# if (sayi1 > sayi2):
#    print("sayi1 sayi2 de büyük")
# elif (sayi1 == sayi2):
#    print("sayi1 sayi2 eşit ")
# else:
#    print("sayi1 sayi2 den küçük")

# username = "hüseyin"
# password = "12345"

# if (username == "hüseyin"): 
#  if (password == "12345"):
#     print("uygulamaya giriş yapıldı.")
#   else:
#     print("parola yanlış")
# else:
# print("username yada parola yanlış")

vize1 = float(input("vize 1 :"))
vize2 = float(input("vize 2 :"))
final = float(input("final : "))

ortalama = ((vize1 + vize2) / 2) * 0.4 + (final * 0.6)
print(ortalama)

# sonuc = ortalama >= 50 and final >= 50

if (ortalama >= 50):
    print("geçtiniz")
else:
    if (final >= 70):
        print("final notu ile geçtiniz")
    else:
        print("kaldınız")
