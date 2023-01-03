x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1-kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir.
a = int(input("1. sayı: "))
b = int(input("2.sayı: "))
result1 = (a * b) - (x + y + z)
# 2-y' nin x'e kalansız bölümünün hesaplayınız
result2 = y // x
# 3-(x,y,z) toplamının mod 3 ' ü nedir
toplam = (x + y + z)
result3 = toplam % 3
# 4-y'nin x. kuvvetini hesaplayınız
result4 = y ** x
# 5-x, *y, z= numbers işlemine göre z' nin küpü kaçtır.
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result5 = z ** 3
# 6- x, *y, z= numbers işlemine göre y ' nin değerleri toplamı kaçtır.
x, *y, z = numbers
result6=y[0]+y[1]+y[2]
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
