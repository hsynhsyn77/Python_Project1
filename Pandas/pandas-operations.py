import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 20, 25],
    "Column3": ["abc", "bcaa", "ade", "cb", "dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x * x

result = df

result = df["Column2"].unique()  # tekrarlayan elemanları kaldırır
result = df["Column2"].nunique()
result = df["Column2"].value_counts()  # herbir elemanın kaç tane tekrarlar
result = df["Column1"] * 2  # eleamnları 2 ile çarpar
result = df["Column1"].apply(kareal)
result = df["Column1"].apply(kareal2)
result = df["Column1"].apply(lambda x: x * x)
df["Column4"] = df["Column3"].apply(len) #her bir elemanın kaç karakter olduğunu verir

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")#sıralanmış olarak gelir
result = df.sort_values("Column3")#alfabetik olur sıralanır
result = df.sort_values("Column3", ascending=False)# tam tersi aşağıdan yukarıya sıralanır

data = {
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap", "Giyim", "Giyim", "Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}

df = pd.DataFrame(data)
print(df)

print(df.pivot_table(index="Ay", columns="Kategori", values="Gelir"))
