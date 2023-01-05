# değiştirilemez
_list=[3,5,7]
_tuples=(1,3,6,7)
print(type(_list))
print(type(_tuples))
# tuple = sıralanabilir, tekrarlanabilir, elemanlar güncellenemez(append, remove)

sonuc=_tuples[0]
sonuc=len(_tuples)
sonuc=len(_list)
_list[0]=10
_list.append(10)

#_tuples[0]=10 yapmaz
sonuc=_tuples+_tuples
sonuc=_tuples+tuple(_list)
print(sonuc)