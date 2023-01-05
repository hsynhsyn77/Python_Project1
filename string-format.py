urunAdi = "elma"
fiyat = 20
miktar = 2.5

# sonuc = str(miktar) + " kg " + urunAdi + " için ödemeniz gereken ücret " +  str(fiyat * miktar) + "TL."

# format methodu
#sonuc = "{} kg {} için ödemeniz gereken ücret {} TL.".format(miktar, urunAdi, (miktar * fiyat))

#f - string
sonuc=f"{miktar}kg {urunAdi} için ödemeniz gereken ücret {miktar*fiyat}"
print(sonuc)
print(sonuc.upper())
