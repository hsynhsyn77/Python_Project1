# 1-100 e kadar

#x = 1
#
#while x <= 100:
#    if x % 2 == 1:
#        print(f"sayı tek : {x}")
#    else:
#        print(f"sayı çift : {x}")
#    x += 1
#print("bitti")

name = ""  # False
while not name.strip():# aslında true
                       # değer üretir isim girmez
                       # enter dersek tekrar isim girin der
    name = input("isminizi giriniz: ")
print(f"Merhaba,{name}")
