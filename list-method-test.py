names=["ali","hüseyin","kaan","gökhan"]
years=[1998,2000,1998,1987]
#1-cenk ismini listenin sonuna ekleyin
names.append("cenk")
print(names)
#2-simay değerini listenin başına ekleyin
names.insert(0,"simay")
print(names)
#3-ali ismini listeden silin
names.remove("ali")
print(names)
#4-gökhan isminin indeksi nedir
index=names.index("gökhan")
print(index)
#5-ali listenin bir elemanımı
names.insert(1,"ali")
result="ali" in names
print(result)
#6-listenin elemanlarını ters çevirin
names.reverse()
print(names)
#7-listenin elemanlarını alfabetik olarak sıralayın
names.sort()
print(names)
#8-years listesini rakamsal olarak sırala
years.sort()
print(years)
#9-str="tofaş,honda" liste içine alın
str="tofaş,honda"
result=str.split(",")
print(result)
#10-years ın en büyük ve en küçük elamanı
yearsMax=max(years)
yearsMin=min(years)
print(yearsMax)
print(yearsMin)
#11-years da kaç tane 1998 var
result=years.count(1998)
print(result)
#12- years ın tüm elemanlarını sil
years.clear()
print(years)
#13-kullanıcıdan aldığınız 3 marka bilgisini bir liste de saklayınız
markalar=[]
marka=input("marka giriniz: ")
markalar.append(marka)
print(markalar)

