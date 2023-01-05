ogrenciler = {

    "120": {
        "ad": "Ali",
        "soyad": "Yılmaz",
        "cep": "5556667778",
    },
    "125": {
        "ad": "Can",
        "soyad": "Korkmaz",
        "cep": "5323344455",
    },
    "128": {
        "ad": "volkan",
        "soyad": "yükselen",
        "cep": "5434444343"
    }

}

# print(ogrenciler["120"]["ad"])
# 1- bilgileri verilen öğrencileri kullanıcıdan aldığımız bilgilerle dictionary içinde saklayınız
# 2-öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.

ogrenciler = {}
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] ={
#   "ad":name,
#  "soyad":surname,
# "telefon":phone
# }

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")
ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print("*"*50)

#2-
ogrNo=input("öğrenci no: ")
ogrenci=ogrenciler[number]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı:{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
