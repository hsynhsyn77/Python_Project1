def sayHello(name=" user"):
    return "Hello" + name


msg = sayHello(" kaan")
msg = sayHello(" simay")

print(msg)


def total(num1, num2):
    return num1 + num2


result = total(10, 20)
result = total(15, 20)
print(result)


def yasHesapla(dogumYılı):
    return 2022 - dogumYılı


ageSimay = yasHesapla(2007)
ageKaan = yasHesapla(2014)
ageBınnur = yasHesapla(1982)
print(ageKaan, ageSimay, ageBınnur)


def emekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRİNG : doğum yılımıza göre emekliliğinize kaç yıl kaldı
    input dogumYili:
    output hesaplanan yıl bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 55 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı...")
    else:
        print("Zaten emekli oldunuz...")


emekliligeKacYilKaldi(1978, "Hüseyin")
emekliligeKacYilKaldi(2004, "kaan")
emekliligeKacYilKaldi(2007, "simay")
emekliligeKacYilKaldi(1982, "binnur")

print(help(emekliligeKacYilKaldi))

list = [1, 2, 3]

print(help(list.append))