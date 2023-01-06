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
    print(type(params))
    """ tek yıldız trub """
    sum = 0
    for n in params:
        sum += n
    return sum


print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 80, 10))

set1 = set([5, 7, 9])
set2 = set([5, 6, 7])
print(set1.symmetric_difference(set2))


def displayUser(**args): """ çift yıldız dictionary olur """


print(type(args))
for key, value in args.items():
    print('{} is {}'.format(key, value))

displayUser(name="çınar", age=2, city="İstanbul")
displayUser(name="ada", age=12, city="kocaeli", phone=123456, mail="huseyin@gmail.com")


def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1="value 1", key2="value 2")
