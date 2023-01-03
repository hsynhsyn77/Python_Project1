def changeName(n):
    n = "simay"


name = "kaan"

changeName(name)
print(name)


def change(n):
    n[0] = "İstanbul"


sehirler = ["konya", "izmir"]

change(sehirler[:])

print(sehirler)


def add(*params):
    sum = 0
    for n in params:
        sum += n
    return sum


print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 80, 10))

set1 = set([5,7,9])
set2 = set([5,6,7])
print(set1.symmetric_difference(set2))
