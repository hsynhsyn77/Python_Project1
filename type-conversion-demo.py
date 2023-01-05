"""
Daire : πr2
Daire Çevre : 2πr
* Yarıçapı verilen bir dairenin alan ve çevresini
hesaplayınız.(r : 3.14)
"""
pi = 3.14
r = float(input("yarı çap : "))
alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan  :" + str(alan) + " çevre: " + str(cevre))
