class veri_b():
    bolum = ""
    bildigi_diller = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = " "


ali = veri_b()
ali.bildigi_diller
ali.bildigi_diller.append("java")
ali.bolum="istatistik"


print("alinin dili: ",  ali.bildigi_diller )

veli = veri_b()
veli.bildigi_diller
veli.bildigi_diller.append("python")
veli.bolum="matematik"
print("velinin dili:" ,veli.bildigi_diller )
print(ali.bolum)
print(veli.bolum)
