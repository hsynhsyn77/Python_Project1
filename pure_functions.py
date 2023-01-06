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
list6 = reduce(lambda a, b: a + b, list5)
print(list6)


