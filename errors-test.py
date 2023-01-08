liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# sayısal değerleri bulma
"""
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue"""
"""
while True:
    sayi=input("sayı : ")
    if sayi=="q":
        break

    try:
        result=float(sayi)
        print("girdiğiniz sayı", result)
        break
    except ValueError:
        print("geçersiz sayı")
        continue 
"""

"""
def checkPassword(parola):
    turkce_karakterler = "şçqüöıi"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez")
        else:
            pass
    print("geçerli parola")

parola=  input("parola : ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)
"""


def factoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("negatif değerler")

    result = 1

    for i in range(1, x + 1):
        result *= i
    return result


for x in [5, 10, 20, -3, "10a"]:

    try:
        y=factoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)

