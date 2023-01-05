msg = "sıfırdan ileri seviye python programlama kursu. ben hüseyin"

sonuc = msg.upper()  # kelimeleribütün harflerini büyük harf yapar
print(sonuc)
sonuc=msg.lower()
print(msg)
sonuc = msg.title()  # kelimeleörin baş harfini büyük yapar
sonuc = msg.capitalize()  # cümlenin ilk kelimesinin baş harfini büyük yapar
print(sonuc)
sonuc=msg.strip() # baş tarafta boşluk var sa gider
sonuc = msg.upper().isupper()  # hepsini büyük harf yaptın mı sorusunu sorar TRUE FALSE
sonuc = " deneme  ".strip()  # boşlukları alır
sonuc = msg.split()  # liste haline döndürür
print(type(sonuc))  # list
sonuc="".join(msg) # birleştirme
print(sonuc)
sonuc = msg.split()
print(sonuc)
sonuc=msg.find("hüseyin")
print(sonuc)
sonuc = msg.index("python")  # kaçıncı indexde başlıyor onu söyler
sonuc = msg.endswith("hüseyin")
sonuc = msg.replace("hüseyin", "mühendisim")
print(sonuc)
sonuc=msg.replace(" ","*")
print(sonuc)
sonuc = msg.lower().replace(" ", "-").replace(".", "-").replace("ı", "i").replace("@", "")
sonuc = "abcd".isalpha()
sonuc = "1abcd".isalpha()
sonuc="123".isdigit()
sonuc=msg.center(70,"*")
print(sonuc)

"""
string method python diye googledan aratarak farklı diğer 
string methodlarına ulaşabiliriz
veya
webscholl.com dan da ulaşabiliriz
"""


