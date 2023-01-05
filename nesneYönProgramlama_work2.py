class veri_bilimci():
    calisanlar = []

    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)


ali = veri_bilimci()
ali.bildigi_diller
ali.bolum

veli = veri_bilimci()
veli.bildigi_diller
veli.bolum

print(dir(veri_bilimci))

veli.dil_ekle("java")
print(veli.bildigi_diller)

ali.dil_ekle("python")
print(ali.bildigi_diller)
