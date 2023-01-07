# Bankamatik Uygulaması

HuseyinHesap = {
    "ad": "Hüseyin Şirikçi",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ekhesap": 2000
}

KaanHesap = {
    "ad": "Kaan Gökhan",
    "hesapNo": "12345678",
    "bakiye": 4000,
    "ekhesap": 1000
}


def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz")
        bakiyeSorgula(KaanHesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı (E/H) : ")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ekHesapKullanilacakMiktar
                print("paranızı alabilirsiniz")
                bakiyeSorgula(KaanHesap)
            else:
                print(f'{hesap["hesapNo"]} no lu hesabınız da {hesap["bakiye"]} bulunmaktadır.')
        else:
            print("Üzgünüz bakiye yetersiz.")
            bakiyeSorgula(KaanHesap)



def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.\nEk hesap limitiniz ise {hesap['ekhesap']} TL.")


paraCek(KaanHesap, 4000)
paraCek(KaanHesap,2000)






