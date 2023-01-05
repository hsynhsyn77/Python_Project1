sehirler = ["istanbul", "maras"]
plakalar = ["34", "46"]
# print(plakalar[0], sehirler[0])
# print(plakalar[1], sehirler[1])

# print(plakalar[0], sehirler[0])
# print(plakalar[1], sehirler[1])

plakalar = {34: "istanbul",
            46: "maras",
            41: "kocaeli"
            }
print(plakalar[41])
print(plakalar[46])

rehber = {
    "hüseyin": ["123456", "123456"],
    "kaan gökhan": {
        "ev": "12345678",
        "iş": "2323232",
        "cep": "454322",
        "adres": {
            "mahalle": "Atatürk mh.",
            "cadde": "selçuklu",
            "no": 35,
            "şehir": "konya"
        }
    }
}
print(rehber["hüseyin"][0])
print(rehber["kaan gökhan"]["ev"])
print(rehber["kaan gökhan"]["adres"]["cadde"])
