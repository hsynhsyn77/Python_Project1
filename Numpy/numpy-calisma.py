import numpy as np

result = np.array([10, 15, 30, 45, 60])

result = np.arange(5, 15)  # 15 dahil olmaz 14 e kadar dizi verir

result = np.arange(50, 100, 5)  # 5 er 5 er artar 100 dahil olmaz

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(0, 100, 5)

result = np.random.randint(10, 30, 5)  # 10 ile 30 arasında rastgele 5 tane sayı

result = np.random.randn(10)  # -1 ile +1 arasında sayı üretir

# result = np.random.randint(10,50,15).reshape(3,5)# 3 e 5 boyunta matris üretir

matris = np.random.randint(-50, 50, 15).reshape(3, 5)
print(matris)

# rowTotal=matris.sum(axis=1)
# colTotal=matris.sum(axis=0)
# print(matris)
# print(rowTotal)
# print(colTotal)

result = matris.max()
result = matris.min()
result = matris.mean()  # ortalama alır

result = matris.argmax()  # en büyüğün index ini verir
result = matris.argmin()

arr = np.arange(10, 20)
print(arr)
result = arr[:3]

result = arr[::-1]  # tersden yazdırır.

result = matris[0]  # matrisin ilk satırı gelir

result = matris[1, 2]

result = matris[:, 0]  # sütünlardaki ilk satırdaki sayıları verir

result = matris ** 2  # her bir elemanın karesi ni alır

ciftler = matris[matris % 2 == 0]  # sadece çift sayıları gösterir
result = ciftler[ciftler > 0]

print(result)
