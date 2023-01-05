meyveler = {"elma", "kiraz", "kavun", "üzüm"}
sebzeler={"bezelye","soğan"}
sonuc = meyveler
# sonuc=meyveler[0] # sıralanamaz, indekslenemez, indekslenemez, indekslenemez

sonuc="elma" in meyveler # true
meyveler.add("muz") # tek bir eleman ekleyeceksek
meyveler.update(["karpuz","vişne"]) # çoklu eleman ekleyeceksek

sonuc=meyveler
sonuc=len(meyveler)
meyveler.remove("karpuz")
print(sonuc)
sonuc=meyveler.pop()
sonuc=meyveler

sonuc=meyveler.union(sebzeler)

for x in meyveler:
    print(x)
print(sonuc)
