p1 = {
    "name": "samsung s20",
    "price": 6000
}
sonuc = p1["name"]
sonuc = p1.get("name")
sonuc = p1.keys()
print(sonuc)
sonuc = p1.values()

print(sonuc)

p1["price"] = 7000
print(sonuc)

sonuc = p1.items()
print(sonuc)

# liste içine alınca for döngüsü yapabiliriz
p1 = {"name": "samsung s20",
      "price": 6000}

#for x in p1.keys():
#    print(x)

#for x in p1.values():
#    print(x)

#    for key, value in p1.items():
#        print(key, value)

p1.update(
    {
        "name":"samsung s20",
        "price": 7000,
        "description": "iyi telefon"
    }
)

print(p1)

p1.popitem()#son ekleneni siler
p1.clear()#hepsini siler
print(p1)
