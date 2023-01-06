# bağımsızlık
A = 9


def impure_sum(b):
    return b + A


def pure_sum(a, b):
    return a + b


print(impure_sum(6))
print(pure_sum(3, 4))


# isimsiz fonksiyonlar (Anonymous Functions)

def old_sum(a, b):
    return a + b


new_sum = lambda a, b: a + b
print(new_sum(4, 5))

sirasiz_liste = [("b", 3), ("a", 8), ("d", 12), ("c", 1)]
print(sirasiz_liste)

print(sorted(sirasiz_liste, key=lambda x: x[1]))

# vektörel operasyonlar (vectorel operations)

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

print(range(0, len(a)))

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
    print(ab)

"""FP"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

print(a * b)

"""map & filter & reduce"""
list1 = [1, 2, 3, 4, 5]

for i in list1:
    print(i + 10)

list2 = list(map(lambda x: x * 10, list1))
print(list2)

"""filter"""
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list4 = list(filter(lambda x: x % 2 == 0, list3))
print(list4)

"""reduce"""
from functools import reduce

list5 = [1, 2, 3, 4]
list6 = reduce(lambda a, b: a * b, list5)  # + , - , /
print(list6)

"""Hatalar / istisnalar (exception)
ZeroDivisionError hatası"""
#a = 10
#b = 0
#
#print(a / b)
#
#try:
#    print(a / b)
#except ZeroDivisionError:
#    print("payda da sıfır olmaz")
#
#"""tip hatası"""
#a = 10
#b = "2"
#
#print(a / b)
#try:
#    print(a / b)
#except TypeError:
#    print("sayi ve string problemi")
#
#a = 10
#b = 2
#print(a / b)
#
#try:
#    print(a / b)
#except TypeError:
#    print("sayi ve string problemi")

A = [[1,2],[3,4],[5,6]]
bbb1=list(map(lambda x: x[0]*3, A))
print(bbb1)

a = [1,2,3]
eee1=list(map(lambda x: x*2, a))
print(eee1)

print(list(filter(lambda x: x < 2, [1,2,3,4,5])))

import numpy as np
a = np.array([1,1,1])
b = np.array([2])

print(a+b)

liste = [1,2,3,4]
A = []

for i in liste:
    A.append(i**2)

print(A)

print(list(map(lambda x: x**2, liste)))

print(list(map(lambda x: x*2, liste)))

A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))

print(list(map(lambda x: x.capitalize(), ["abc","bcd","cde"])))


def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")

yap(1,2,0)

A = ["ali", "veli", "isik"]
B = [1, 2, 3]
AB = [A, B]

for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x - 3, i)))


A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))

